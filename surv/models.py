from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from pyomo.solvers.tests.mip.test_asl import mock_all


class person(models.Model):
    first_name=models.CharField(max_length=150 ,default=None,null=True)
    last_name=models.CharField(max_length=150,null=True)
    phone_number=models.CharField(max_length=20,null=True)
    Email=models.EmailField(null=True)
    role=models.IntegerField(max_length=1,default=0,null=True)
    password=models.CharField(max_length=150 ,default=None,null=True)
    incentive=models.BooleanField(default=False,null=True)


class Source(models.Model):
    SName = models.CharField(max_length=150)
    Logo = models.ImageField(upload_to='pictures/Source_logos/', blank=False)
    Admin=models.ForeignKey(person,on_delete=models.CASCADE,default=None)


class Branch(models.Model):
    BName = models.CharField(max_length=150)
    Source_fk = models.ForeignKey(Source, on_delete=models.CASCADE, default=None)
    Num_waiters = models.IntegerField()


class Waiters(models.Model):
    W_Name = models.CharField(max_length=150)
    Branch_fk = models.ForeignKey(Branch, on_delete=models.CASCADE, default=None)
    W_photo = models.ImageField(upload_to='pictures/waiters_photos/', blank=False)


class Ask(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()
    is_visible = models.BooleanField()
    Answer_type = models.TextField()
    Source_fk = models.ForeignKey(Source, on_delete=models.CASCADE, default=None)


class Ans(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # done = models.BooleanField()
    rate = models.CharField(max_length=1)
    Answer_comment = models.TextField(default=None)
    Waiter_fk = models.ForeignKey(Waiters, on_delete=models.CASCADE, default=None)
    Time = models.TimeField(blank=False, default=None)
    Date = models.DateField(blank=False, default=None)
    # Time_Date=models.DateTimeField()
    Question_id = models.ForeignKey(Ask, on_delete=models.CASCADE, default=None)



