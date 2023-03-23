from django.urls import path
from . import views
from .views import SignUpView
from .views import register
from django.contrib.auth.models import User


urlpatterns = [

    #SITE
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),

    #USER
    path('signup/', SignUpView.as_view(), name='signup'),
    path("password_change/", views.PasswordChange.as_view(), name='password_change'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('register/', register, name='register'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('user/<int:pk>/update', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/delete', views.UserDelete.as_view(), name='user_delete'),
    path('stats/', views.stats, name='stats'),

]