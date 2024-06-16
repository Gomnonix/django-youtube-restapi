# django-youtube-restapi
Docker란: https://www.notion.so/docker-f89977994ec64ba39e6e32e1aa6316a9


## (1) Project Settings

-Github

## Model 구조 => ORM

(1) User => users (모델을 만들 떄)
- email
- password
- nickname
- is_business

(2) Video => videos
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
- User: FK
- Video: FK
- reaction (like, dislike, cancel) => 실제 youtube rest api

(4) Comment => comments
- User: FK
- Video: FK
- content
- like
- dislike

(5) Subscription
- User: FK => subscriber (내가 구독한 사람)
- User: FK => subscriber (나를 구독한 사람)

(6) Common
- created_at
- updated_at

모델을 먼저 정의한 이유는 Django -> DB migration(테이블 구조 정의) -> REST API
