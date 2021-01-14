from django.urls import path

from .views import CreateSubscriptionView, ListSubscriptionView


app_name = 'user'

urlpatterns = [
    path(
        'subscription/', CreateSubscriptionView.as_view(), 
        name='subscription'),
    path(
        'list-subscription/', ListSubscriptionView.as_view(), 
        name='list_subscription'),
]