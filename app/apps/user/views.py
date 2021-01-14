from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Subscription
from .serializers import SubscriptionSerializer


# Create your views here.

class CreateSubscriptionView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (AllowAny,)


class ListSubscriptionView(ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)