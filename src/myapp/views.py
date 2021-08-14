from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import About
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        #send an email
        send_mail(
            subject, 
            message,
            name,
            ['ransquophi@gmail.com'], 
            )
        
       # return render(request, 'contact.html',{name:name})
        # context = {
        #     'name': name,
        #     'email': email,
        # 'subject': subject,
        # 'message': message
        # }
        return render(request, 'contact.html',{'name':name})
    else:
        return render(request, 'contact.html',context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def portfolio(request):
    return render(request, 'portfolio.html')

def resume(request):
    return render(request, 'resume.html')

def services(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'services.html', context)