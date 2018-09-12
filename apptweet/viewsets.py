from rest_framework import viewsets
from apptweet.models import Tweet
from apptweet.serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """Viewset de Tweet."""
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
