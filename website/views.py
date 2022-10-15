from django.shortcuts import render, redirect
from .models import Services, Portfolio, ContactUs
from django.contrib import messages

# Create your views here.

def index(request):

    # Contact Form Submission
    if request.method == 'POST':

        contact = ContactUs()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message

        if not name:
            messages.error(request, 'Please fill all fields')
            return redirect('/#contact')
        elif not email:
            messages.error(request, 'Please fill all fields')
            return redirect('/#contact')
        elif not message:
            messages.error(request, 'Please fill all fields')
            return redirect('/#contact')
        else:
            contact.save()
            messages.success(request, 'Form Submitted Successfully!!!')
            return redirect('/#contact')
            
    # Services, Portfolio data from database to html    
    context = Services.objects.all()
    portfolio = Portfolio.objects.all()
    return render(request, 'index.html', {'context':context, 'portfolio':portfolio})

