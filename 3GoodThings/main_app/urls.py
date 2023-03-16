from django.urls import path
from . import views

urlpatterns = [

    #SITE
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('profile/', views.profile, name='profile'),
    path('stats/', views.stats, name='stats'),

    #USER
    # path('register/', views.register_request, name='register'),
    # path('signup/', SignUpView.as_view(), name='signup'),


]
