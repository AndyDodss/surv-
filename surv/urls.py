from django.urls import re_path ,path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
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
    path('scann', views.scann, name='scann'),
    path('scanndemo', views.scanndemo, name='scanndemo'),
    path('thanks', views.thanks, name='thanks'),
    path('signup', views.signup, name='signup'),
    path('tosignup', views.tosignup, name='tosignup'),
    path('login', views.login, name='login'),
    path('tologin', views.tologin, name='tologin'),
    path('logout', views.logout, name='logout'),
 #   path('count', views.count, name='count' ),
re_path('answ',views.answ,name='answ'),

    re_path(r'^(?P<qr>[a-z]*[0-9]*)/place=((?P<place>[0-9]))&branch=((?P<branch>[0-9]))&server=((?P<waiter>[0-9]))', views.scann_info, name='scann'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)