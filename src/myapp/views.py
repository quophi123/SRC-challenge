from django.shortcuts import render
from django.http import HttpResponse
from .models import About
# Create your views here.

def home(request):
    abt = About.objects.all()
    context = {
        'name': abt
    }
    return render(request, 'home.html',context)