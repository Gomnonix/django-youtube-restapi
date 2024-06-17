from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q

# - User: FK
# - Video: Fk
# - reaction (like, dislike, cancel) => choice
class Reaction(CommonModel):
    # circular import error
    # user = models.ForeignKey(User, ) 
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTON_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    # column: reactions -> migration -> reaction -> migration
    reaction = models.IntegerField(
        choices=REACTON_CHOICES,
        default=NO_REACTION
    )

    @staticmethod
    def get_video_reactions(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count=Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count=Count('pk', filter=Q(reaction=Reaction.DISLIKE))
        )
        return reactions