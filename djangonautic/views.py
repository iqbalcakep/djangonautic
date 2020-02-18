from django.http import HttpResponse
from django.shortcuts import render

def about(req): 
    return HttpResponse('about')
   

def homepage(req): 
    # return HttpResponse('homepage')
     return render(req,'homepage.html')