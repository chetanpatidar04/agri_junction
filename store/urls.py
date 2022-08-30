from django.contrib import admin
from django.urls import path
from .views import index,signup,customer_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index, name="homepage"),
    path('signup',signup),
    path('login',customer_login),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)