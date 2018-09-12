"""Urls AppTweet."""

from django.urls import path
from apptweet.viewsets import TweetViewSet

urlpatterns = [
    path('', TweetViewSet)
]
