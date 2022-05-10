from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('sub/', views.sub, name = 'sub'),
]