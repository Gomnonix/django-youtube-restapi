from django.db import models

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # 다른 모델들이 상속 받게 만든다.
        abstract = True # DB에 테이블을 추가하지 마시오.
