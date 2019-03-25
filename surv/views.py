from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate
from collections import OrderedDict
import regex as re

def home(request):

    return render(request,'home.html')