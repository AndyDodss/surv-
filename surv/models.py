from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Ask(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()
    is_visible = models.BooleanField()

    def __str__(self):
        return "Su"


class Ans(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    done = models.BooleanField()
    rate = models.CharField(max_length=1)
    Question_id = models.ForeignKey(Ask, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "S"

