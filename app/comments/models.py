from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Comment(CommonModel):
    # User:Comment => 1:N
    # - User => Comment, Comment, Comment, Comment (O)
    # - Comment => User, User, User (X)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    # Video:Comment(FK) => 1:N
    # - Video => Comment, Comment, Comment => O
    # - Comment => Video(침착맨), Video(이지금), Video(잇섭) => X
    # Video -> video (migration->migrate)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    #video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)
    
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # docker-compose run --rm app sh -c 'python manage.py makemigrations'
    # docker-compose run --rm app sh -c 'python manage.py migrate'

