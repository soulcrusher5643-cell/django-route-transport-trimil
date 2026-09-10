from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Register

def home_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            return redirect('admin_dashboard')
        return redirect('user_dashboard')
    return render(request, 'home.html', {'active_page': 'home'})

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('Sign_In')
    if request.user.is_staff or request.user.is_superuser:
        return redirect('admin_dashboard')
    return redirect('user_dashboard')

@login_required
def admin_dashboard(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return redirect('user_dashboard')
    users_list = Register.objects.all().order_by('-date_joined')
    total_users = users_list.count()
    context = {
        'active_page': 'admin_dashboard',
        'users_list': users_list,
        'total_users': total_users,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def user_dashboard(request):
    context = {
        'active_page': 'user_dashboard',
    }
    return render(request, 'user_dashboard.html', context)

def contact_view(request):
    context = {'active_page': 'contact'}
    if request.method == 'POST':
        context['success_message'] = "Thank you! Your inquiry has been submitted successfully."
    return render(request, 'contact.html', context)

def Sign_In(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
        else:
            return render(request, 'Sign_In.html', {'error': 'Invalid username or password', 'active_page': 'signin'})
    return render(request, 'Sign_In.html', {'active_page': 'signin'})
        
def Sign_Up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        password = request.POST.get('password')
        username = request.POST.get('username')
        age_val = int(age) if age and str(age).isdigit() else 0
        user = Register.objects.create_user(username=username, password=password, name=name, age=age_val)
        return redirect('Sign_In')
    return render(request, 'Sign_Up.html', {'active_page': 'signup'})

def Signout(request):
    logout(request)
    return redirect('Sign_In')