from django.contrib import admin
from django.urls import path, include
from skills import views
urlpatterns = [
    path('skills', views.skills, name='skills'),
    
]