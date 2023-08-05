from django.db import models
from users.models import User

# Create your models here.


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="recipient", on_delete=models.CASCADE)


class Friends(models.Model):
    user_id_1 = models.ForeignKey(User, related_name="user_id_1", on_delete=models.CASCADE)
    user_id_2 = models.ForeignKey(User, related_name="user_id_2", on_delete=models.CASCADE)
