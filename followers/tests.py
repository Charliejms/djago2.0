from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from followers.models import Relationship
from followers.utils import get_followers, get_followers_v2, get_following


class RelationshipTests(TestCase):

    def setUp(self):
        """
        Se ejecuta antes de cada test
        :return: Objeto de pruebas
        """
        self.user1 = User.objects.create_user('javiercs', 'javier.cacuango@gmail.com', 'Django13')
        self.user2 = User.objects.create_user('mariagb', 'maria.garrido.boscana@gmail.com', 'Django13')

        Relationship.objects.create(origin=self.user1, target=self.user2)

    def test_get_followers_returns_users_that_follow_by_a_given_user(self):
        followers = get_followers_v2(self.user2)

        self.assertEquals([self.user1], followers) # followers ==[user1]

    def test_get_following_returns_users_that_a_given_user_follows(self):
        following = get_following(self.user1)

        self.assertEquals([self.user2], following)
