from django.contrib.auth.models import User
from django.test import TestCase, override_settings

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from followers.models import Relationship
from followers.utils import get_followers, get_followers_v2, get_following


class RelationshipTests(TestCase):

    USER_PASSWORD = 'Django13'

    def setUp(self):
        """
        Se ejecuta antes de cada test
        :return: Objeto de pruebas
        """
        self.user1 = User.objects.create_user('javiercs', 'javier.cacuango@gmail.com', self.USER_PASSWORD)
        self.user2 = User.objects.create_user('mariagb', 'maria.garrido.boscana@gmail.com', self.USER_PASSWORD)

        Relationship.objects.create(origin=self.user1, target=self.user2)

    def test_get_followers_returns_users_that_follow_by_a_given_user(self):
        followers = get_followers_v2(self.user2)

        self.assertEquals([self.user1], followers) # followers ==[user1]

    def test_get_following_returns_users_that_a_given_user_follows(self):
        following = get_following(self.user1)

        self.assertEquals([self.user2], following)


@override_settings(ROOT_URLCONF='followers.urls')
class APITests(APITestCase):

    FOLLOWING_API_URL = '/following/'
    USER_PASSWORD = 'Django13'

    def setUp(self):
        # setup
        self.user1 = User.objects.create_user('javiercs', 'javier.cacuango@gmail.com', self.USER_PASSWORD)
        self.user2 = User.objects.create_user('mariagb', 'maria.garrido.boscana@gmail.com', self.USER_PASSWORD)
        self.user3 = User.objects.create_user('charliedev', 'charliedev@gmail.com', self.USER_PASSWORD)
        self.user4 = User.objects.create_user('nuriagb', 'mariagb@gmail.com', self.USER_PASSWORD)

        Relationship.objects.create(origin=self.user1, target=self.user2)
        Relationship.objects.create(origin=self.user1, target=self.user3)
        Relationship.objects.create(origin=self.user1, target=self.user4)


    def test_following_users_endpoint_fails_when_user_is_not_authenticated(self):

        # actions
        response = self.client.get(self.FOLLOWING_API_URL)
        # assert
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_doesnot_follow_any_user_and_return_empty_list_is_returned(self):
        # authenticate user1
        self.client.login(username=self.user2.username, password=self.USER_PASSWORD)
        # action
        response = self.client.get(self.FOLLOWING_API_URL)
        # assert response 200 Ok
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # assert data is empty
        self.assertEquals(len(response.data), 0)

    def test_user_follows_3_users_and_3_users_are_returned(self):

        # authenticate user1
        self.client.login(username=self.user1.username, password=self.USER_PASSWORD)
        # action
        response = self.client.get(self.FOLLOWING_API_URL)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # assert data is empty
        self.assertEquals(len(response.data), 3)
