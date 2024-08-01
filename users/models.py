from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import BaseModel, Timestamps
from users.managers import UserManager
import secrets

# Create your models here.
class User(AbstractUser, BaseModel, Timestamps):
    objects = UserManager()

    def get_auth_token(self):
        if not Token.objects.filter(user=self).exists():
            token = Token.objects.create(user=self, key=secrets.token_hex(20))
            return token.key
        else:
            token = Token.objects.filter(user=self).update(key=secrets.token_hex(20))
            token = self.auth_token
            return token.key


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auth_token')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
