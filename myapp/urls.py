from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('signup/', views.Sign_Up, name='Sign_Up'),
    path('signin/', views.Sign_In, name='Sign_In'), 
    path('logout/', views.Signout, name='logout'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]