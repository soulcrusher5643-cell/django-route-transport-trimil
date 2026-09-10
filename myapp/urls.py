from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/user/', views.user_dashboard, name='user_dashboard'),
    path('signup/', views.Sign_Up, name='Sign_Up'),
    path('signin/', views.Sign_In, name='Sign_In'), 
    path('logout/', views.Signout, name='logout'),
    path('contact/', views.contact_view, name='contact'),
]