from django.db import models
from common.models import CommonModel
from users.models import User

# - title
# - description 
# - link
# - views_count
# - thumbnail
# - video_file
# - User: FK (누가 만들었는가)
class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True) 
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # S3 Bucket -> Save File -> URL -> Save URL
    video_file = models.FileField(upload_to='storage/') # 파일을 저장하는 방법
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 운영의 문제

# User : Video 관계 => 1:N => 부모:자녀(FK)
    # => User : Video, Video, Video ... (가능o)
    # => Video : User, User, ... (불가능x)