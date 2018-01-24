# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from followers.views import FollowingViewSet

router = SimpleRouter()
router.register('following', FollowingViewSet, base_name='following')

urlpatterns = router.urls
