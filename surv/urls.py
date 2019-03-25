from django.urls import re_path ,path,include
from . import views

urlpatterns = [
    path('home',views.home,name='home')
]