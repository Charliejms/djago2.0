# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from followers.views import FollowingViewSet, FollowViewSet

router = SimpleRouter()
router.register('following', FollowingViewSet, base_name='following')
router.register('follow', FollowViewSet)

urlpatterns = router.urls
