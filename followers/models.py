from django.contrib.auth.models import User
from django.db import models


class Relationship(models.Model):
    # unique_together = ("origin", "target") # works with postgresql and mysql
    origin = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='relationship_origin')  # If "parent" rec gone, delete "child" rec!!!
    target = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='relationship_target')  # usuario al que sigue
    create_at = models.DateTimeField(auto_now_add=True)
