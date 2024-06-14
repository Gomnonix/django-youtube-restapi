from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser, #User를 상속 받도록 한다
        PermissionsMixin, # super user, 일반 user를 구분하기 위해
        BaseUserManager
    )


class UserManager(BaseUserManager):
    # 일반 유저 생성 함수
    def create_user(self, email, password):
        if not email:
            raise ValueError("Please enter your email address")
        
        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user

    # 슈퍼 유저 생성 함수
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    

    # docker-compose run --rm app sh -c 'python manage.py test users'
    # docker-compose run --rm app sh -c 'python manage.py makemigrations'
    # docker-compose run --rm app sh -c 'python manage.py migrate'
    # docker-compose run --rm app sh -c 'python manage.py showmigrations': 디버깅) 유저 충돌 문제 해결 방법
    # docker-compose run --rm app sh -c 'python manage.py createsuperuser', 슈퍼 user 생성

# - email
# - password
# - nickname
# - is_business
class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=15)
    is_bussiness = models.BooleanField(default=False) # default

    # PermissionMixin: 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' #USERNAME_FIELD로 정의가 되어있는 필드는 unique=True가 필요

    objects = UserManager() # 유저를 생성 및 관리 (유저를 구분해서 관리하기 위해 - 관리자계정, 일반계정)

    def __str__(self): # 핵심 데이터를 볼 수 있게 설정
        return f'email: {self.email}, nickname: {self.nickname}'
