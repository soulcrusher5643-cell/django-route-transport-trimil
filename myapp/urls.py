from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),  # Route to /home 
    path('about/', views.about_view, name='about'),  # Route to /about 
    path('contact/', views.contact_view, name='contact'),  # Route to /contact 
]