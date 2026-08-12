from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Register

# Create your views here.
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html', {'active_page': 'home'})

def about_view(request):
    return render(request, 'about.html', {'active_page': 'about'})

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
            return redirect('home')
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
        Register.objects.create_user(username=username, password=password, name=name, age=age_val)
        return redirect('Sign_In')
    return render(request, 'Sign_Up.html', {'active_page': 'signup'})

def Signout(request):
    logout(request)
    return redirect('Sign_In')