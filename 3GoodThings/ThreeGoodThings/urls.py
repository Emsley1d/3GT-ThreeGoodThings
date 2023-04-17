from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('main_app/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('password_reset', TemplateView.as_view(template_name='password_reset_form.html'), name="password_reset_form"),
]
