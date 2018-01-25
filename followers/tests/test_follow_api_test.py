# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import override_settings

from rest_framework import status
from rest_framework.test import APITestCase

from followers.models import Relationship


@override_settings(ROOT_URLCONF='followers.urls')
class FollowAPITests(APITestCase):

    USER_PASSWORD = 'Django13'
    FOLLOW_API_URL = '/follow/'

    def setUp(self):
        self.user1 = User.objects.create_user('javiercs', 'javiercs@gmail.com', self.USER_PASSWORD)
        self.user2 = User.objects.create_user('mariagb', 'mariagb@gmail.com', self.USER_PASSWORD)

    def test_endpoint_returns_403_when_user_is_not_autehnticated(self):

        response = self.client.post(self.FOLLOW_API_URL, {})
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_endpoint_returns_400_bad_request_when_no_target_user_is_send(self):
        self.client.login(username=self.user1.username, password=self.USER_PASSWORD)

        response = self.client.post(self.FOLLOW_API_URL, {})
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("target", response.data)
        self.assertEquals(response.data.get('target')[0], 'This field is required.')

    def test_endpoint_returns_400_bad_request_when_target_user_doesnot_exist(self):
        self.client.login(username=self.user1.username, password=self.USER_PASSWORD)

        # actions
        response = self.client.post(self.FOLLOW_API_URL, {"target": 0})

        # assert
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('target', response.data)
        self.assertEquals(response.data.get('target'), ['Invalid pk "0" - object does not exist.'])

    def test_endpoint_returns_400_bad_request_when_target_user_is_already_followed(self):
        self.client.login(username=self.user1.username, password=self.USER_PASSWORD)
        Relationship.objects.create(origin=self.user1, target=self.user2)
        data_request = {
            'target': self.user2.pk
        }
        # action
        response = self.client.post(self.FOLLOW_API_URL, data_request)
        # assert
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data.get('non_field_errors'), ['You already follow this user.'])

    def test_endpoint_returns_201_create_when_target_user_is_not_follow(self):
        self.client.login(username=self.user1.username, password=self.USER_PASSWORD)
        # action
        response = self.client.post(self.FOLLOW_API_URL, {'target': self.user2.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Relationship.objects.filter(origin=self.user1, target=self.user2).exists())

    def test_endpoint_retunrs_400_bad_request_when_user_follow_itself(self):
        self.client.login(username=self.user1.username, password=self.USER_PASSWORD)
        response = self.client.post(self.FOLLOW_API_URL, {'target': self.user1.pk})
        # assert
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data.get('non_field_errors'), ['You can not follow yourself.'])



