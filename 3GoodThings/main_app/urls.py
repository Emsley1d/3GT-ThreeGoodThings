from django.urls import path
from . import views
from .views import SignUpView
from .views import register

urlpatterns = [

    #SITE
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('profile/', views.profile, name='profile'),
    path('stats/', views.stats, name='stats'),

    #USER
    path('signup/', SignUpView.as_view(), name='signup'),
    path("password_change/", views.PasswordChange.as_view(), name='password_change'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('register/', register, name='register'),

]