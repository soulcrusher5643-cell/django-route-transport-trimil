from django.shortcuts import render

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