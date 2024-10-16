from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from hrd.views import register, applicant_create_view


# Redirect to admin
def redirect_to_admin(request):
    return redirect('/dashboard/')

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('redirect/', redirect_to_admin, name='redirect'),
    path('dashboard/', admin.site.urls),
    path('applicant/new/', applicant_create_view, name='applicant_create'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)