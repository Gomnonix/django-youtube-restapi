from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription, User
from .serializers import SubscriptionSerializer
from rest_framework.exceptions import ValidationError
from django.db.models import Q

class SubscriptionList(APIView):
    def post(self, request):
        subscriber = request.user
        subscribed_to_id = request.data.get('subscribed_to')

        if subscriber.id == subscribed_to_id or Subscription.objects.filter(subscriber=subscriber, subscribed_to_id=subscribed_to_id).exists():
            return Response({"error": "Invalid subscription request."}, status=status.HTTP_400_BAD_REQUEST)

        request.data['subscriber'] = subscriber.id
        serializer = SubscriptionSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionDetail(APIView):
    def delete(self, request, pk):
        subscriber = request.user
        subscription = get_object_or_404(Subscription, Q(subscriber=subscriber) & Q(subscribed_to=pk))
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)