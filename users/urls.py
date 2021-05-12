"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # 登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name="login"),
    url(r'^logout/$', views.logout_view, name='logout'),
    
    # 注册页面
    url(r'^register/$', views.register, name='register'),
]