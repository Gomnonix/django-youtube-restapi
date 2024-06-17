# Vevio REST API 관련 테스트
from rest_framework.test import APITestCase
from users.models import User
from .models import Video
from django.urls import reverse # url => name을 기반으로 url 값을 불러온다.
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import pdb # python debugger

class VideoAPITestCase(APITestCase):
    # 테스트 코드가 실행되기 전 동작하는 함수
    # 테스트 전 데이터를 생성하는 역할
    # (1) 유저 생성/로그인 -> (2) 비디오 생성
    def setUp(self):
        self.user = User.objects.create_user(
            email='giung@gmail.com',
            password='password123'
        )

        # 로그인
        self.client.login(email='giung@gmail.com', password='password123')

        self.video = Video.objects.create(
            title='test video',
            link='http://www.test.com',
            user=self.user
        )

    # 127.0.0.1:8000/api/v1/video [GET]
    def test_video_list_get(self):
        # url = 'http://127.0.0.1:8000/api/v2/video'
        url = reverse('video-list')
        res = self.client.get(url) # 전체 비디오 조회 데이터
    
        #self.assertEqual(res.status_code, 200)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertTrue(len(res.data) > 0)

        # title 컬럼이 응답 데이터에 잘 들어가 있는지 확인
        # res.data = [video1, video2, ....]
        for video in res.data:
            self.assertIn('title', video)

    # 비디오 생성
    def test_video_list_post(self):
        url = reverse('video-list') # api/v1/video

        data = {
            'title':'test video title',
            'link':'http://test.com',
            'category':'test category',
            'thumbnail':'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }

        res = self.client.post(url, data) #VideoList [POST]

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video title')

    # 특정 비디오 조회
    def test_video_detail_get(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk}) # url: api/v1/video/1
        res = self.client.get(url) # [GET] api/v1/video/1

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # 특정 비디오 업데이트
    def test_video_detail_put(self):       
        url = reverse('video-detail', kwargs={'pk':self.video.pk})

        data = {
            'title':'updated video',
            'link':'http://test.com',
            'category':'test category',
            'thumbnail':'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }
        
        res = self.client.put(url, data) # 서버에 요청 -> res

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'updated video')      

    # 특정 비디오 삭제
    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        res = self.client.delete(url) # [DELETE] api/v1/video/{pk} -> REST API
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        res = self.client.get(url) # [GET] api/v1/video/{pk}
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    # 테스트 코드 실행
    # docker-compose run --rm app sh -c 'python manage.py test videos'