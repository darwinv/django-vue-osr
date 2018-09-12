from rest_framework import routers
from apptweet.viewsets import TweetViewSet

router = routers.DefaultRouter()

router.register(r'', TweetViewSet)
