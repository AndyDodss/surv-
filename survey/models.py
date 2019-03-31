from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Source(models.Model):
    SName=models.TextField()
    Logo=models.ImageField()
class Branch(models.Model):
    BName=models.TextField()
    Source_fk=models.ForeignKey(Source,on_delete=models.CASCADE,default=None)
    Num_waiters=models.IntegerField()
class Waiters(models.Model):
    W_Name=models.TextField()
    Branch_fk=models.ForeignKey(Branch,on_delete=models.CASCADE,default=None)
    W_photo=models.ImageField()

class Ask(models.Model):

    name = models.CharField(max_length=150)
    content = models.TextField()
    is_visible=models.BooleanField()
    Answer_type=models.TextField()
    Source_fk=models.ForeignKey(Source,on_delete=models.CASCADE,default=None)


class Ans(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    done = models.BooleanField()
    rate = models.CharField(max_length = 1)
    Answer_comment=models.TextField()
    Waiter_fk=models.ForeignKey(Waiters,on_delete=models.CASCADE,default=None)
    Time=models.TimeField()
    Date=models.DateField()
    #Time_Date=models.DateTimeField()
    Question_id=models.ForeignKey(Ask,on_delete=models.CASCADE,default=None)
   


