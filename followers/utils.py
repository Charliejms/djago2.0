# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

# Models
from followers.models import Relationship


def get_followers(user):
    # devuelve una lista con los PK de los usarios de las relaciones en las que el usuario <user> es una relationship_target
    # SELECT origen_id FROM relationship WHERE target_id = user_id
    followers_pks = user.relationship_target.all().values_list('origin', flat=True)
    return list(User.objects.filter(pk__in=followers_pks))  # SELECT * FROM users WHERE id IN (followers_pks)


def get_followers_v2(user):
    relationships = Relationship.objects.filter(target=user).select_related('origin')
    followers = list()
    for relationship in relationships:
        followers.append(relationship.origin)
    return followers


def get_following(user):
    relatinships = Relationship.objects.filter(origin=user).select_related('target')
    following = list()
    for relatinship in relatinships:
        following.append(relatinship.target)
    return following