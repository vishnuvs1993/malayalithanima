from django.shortcuts import render
from django.http import HttpResponse
 


def index(request):
    return render(request,'home.html')
def sample(request):
    return render(request,'customerlogin.html')    
