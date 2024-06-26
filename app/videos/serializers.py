from rest_framework import serializers
#from rest_framwork.serializers import ModelSerializer
from .models import Video
from reactions.models import Reaction
from users.serializers import UserInfoSerializer
from comments.serializers import CommentSerializer
from users.models import User


class VideoListSerializer(serializers.ModelSerializer):
    # Video:User => Video(FK) -> User
    user = UserInfoSerializer(read_only=True) # Video(FK)
    class Meta:
        model = Video
        fields = "__all__"
        depth = 1

class VideoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    description = serializers.CharField() 
    link = serializers.URLField()
    category = serializers.CharField(max_length=20)
    views_count = serializers.IntegerField(default=0)
    thumbnail = serializers.URLField() 
    video_file = serializers.FileField()
    user_id = serializers.IntegerField()
    # 일반 사용자로 부터 user 인스턴스를 받을 수 없기에 user 식별자인 => user_id를 직렬화 해서
    # 따로 user 인스턴스를 get한 뒤에 video 객체를 저장

    
    def create(self, validated_data):
        user = User.objects.get(id=validated_data["user_id"])
        validated_data["user"] = user
        # return Video.(title, description, link, views_count, thumbnail, video_file)
        return Video.objects.create(**validated_data)


class VideoDetailSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True) # Video(FK)

    # Video:Comment => Video -> Comment(FK)
    # - Reverse Accessor = 부모가 자녀를 찾을 때 활용
    # - 부모가 자녀를 찾을 때 => _set으로 부모에 속한 자녀들을 모두 찾을 수 있다.
    # - reverse accese라 _set있어야 인식가능
    comment_set = CommentSerializer(many=True, read_only=True) 

    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1

    def get_reactions(self, video):
        return Reaction.get_video_reactions(video) # 비디오 줄게 -> 리액션 내놔.


# docker-compose run --rm app sh -c 'python manage.py makemigrations'
# docker-compose run --rm app sh -c 'python manage.py migrate'
    
# 여기서 질문! 어드민으로 해서 좋아요 카운트를 올려봤는데 like_count가 안들어가네요.. ;;