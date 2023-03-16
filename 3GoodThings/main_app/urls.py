from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('profile/', views.profile, name='profile'),
    path('stats/', views.stats, name='stats'),
    path('days/', views.days_index, name='days'),




]
