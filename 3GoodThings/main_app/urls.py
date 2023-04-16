from django.urls import path
from . import views
from .views import SignUpView
from .views import UserDelete
from .views import register
from django.contrib.auth.models import User
from .views import UserDetail



urlpatterns = [

    #SITE
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),

    #USER
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('change-password/', views.PasswordChangeView.as_view(), name='password_change'),
    path('change-password/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('register/', register, name='register'),
    path('user/<int:pk>/detail', views.UserDetail.as_view(), name='detail'),
    path('user/<int:pk>/update', views.UserUpdate.as_view(), name='update'),
    path('user/<int:pk>/delete', views.UserDelete.as_view(), name='delete'),
    path('user/<int:pk>/', UserDetail.as_view(), name='detail'),

]