from django.urls import path
from .views import SubscriptionList, SubscriptionDetail

urlpatterns = [
    path('', SubscriptionList.as_view(), name='subscription-list'),
    path('<int:pk>/', SubscriptionDetail.as_view(), name='subscription-detail'),
]