# django-youtube-restapi
Docker란: https://www.notion.so/docker-f89977994ec64ba39e6e32e1aa6316a9

CI/CD, GitHub Actions, PostgreSQL: https://www.notion.so/CI-CD-861e95b69421468b862b93423b8dc1a6

## (1) Project Settings

-Github

## Model 구조 => ORM

(1) User => users (모델을 만들 떄) 
- 역할: 사용자 정보를 저장하고 관리합니다.
- email
- password
- nickname
- is_business

(2) Video => videos
- 역할: 업로드된 동영상 정보를 저장하고 관리합니다.
- title
- description 
- link
- views_count
- thumbnail
- video_file
- User: FK (누가 만들었는가)

ex) 파일(이미지, 동영상) 
=> 장고에 부하가 걸림
=> S3 Bucket(저렴, 속도가 빠름) -> 결과물: 링크

(3) Reaction => reactions
- 역할: 사용자 반응(좋아요, 싫어요 등)을 저장하고 관리합니다.
- User: FK
- Video: FK
- reaction (like, dislike, cancel) => 실제 youtube rest api

(4) Comment => comments
- 역할:  동영상에 작성된 댓글을 관리하는 모델. 각 댓글의 내용, 작성자, 작성일, 좋아요 수 등을 저장
- User: FK
- Video: FK
- content
- like
- dislike

(5) Subscription: 
- 역할: 사용자들이 채널을 구독하는 관계를 나타내는 모델. 구독자와 구독 대상 채널 사이의 관계를 저장
- User: FK => subscriber (내가 구독한 사람)
- User: FK => subscriber (나를 구독한 사람)

(6) Common
- 역할: 공통적으로 사용되는 정보나 기능을 담당하는 모델
- created_at
- updated_at

모델을 먼저 정의한 이유는 Django -> DB migration(테이블 구조 정의) -> REST API
