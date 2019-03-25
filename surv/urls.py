from django.urls import re_path ,path,include
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    re_path(r'^myadmin', views.index, name='index' ),
    path('create/', views.create, name='create' ),
    path('add_question/', views.add_question, name='add_question' ),
    path('delete/<id>/', views.delete, name='delete' ),
    path('register', views.register, name='register' ),
    path('login_check', views.login_check, name='login_check' ),
    path('answer',views.answer,name='answer'),
    path('ans', views.ans, name='ans' ),
    re_path(r'^testall', views.testall, name='test' ),
    re_path(r'^/testall', views.testall, name='test' ),
    re_path(r'^test', views.group, name='group' ),
    re_path(r'^/test', views.group, name='group' ),
    path('', views.home, name='home'),
 #   path('scann', views.scann, name='scann'),
 #   path('count', views.count, name='count' ),
    path('chart', views.chart, name='chart'),
]