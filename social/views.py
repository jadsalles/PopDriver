from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def login(request):

    context={}
    
    return render(request, 'social/login.html', context)

