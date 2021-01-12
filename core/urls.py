from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('education', views.education, name='eduction'),
    path('skills', views.skills, name='skills'),
    path('contact', views.contact, name='contact'),    
]
