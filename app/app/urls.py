from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import ( # 우리가 만든 이미지에는 추가 되어있기에 노란색 밑줄은 신경 안써도 됨)
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView
)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/videos/', include('videos.urls')),
    path('api/v1/subscriptions/', include('subscriptions.urls'))
]

urlpatterns += static(
    # URL의 접두어가 MEDIA_URL일 때는 정적파일을 돌려준다.
    prefix=settings.MEDIA_URL,
    # 돌려줄 디렉터리는 MEDIA_ROOT를 기준으로 한다.
    document_root=settings.MEDIA_ROOT,
)