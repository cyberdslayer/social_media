from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def login_view(request):
    '''login page'''
    
    
    return HttpResponse("This is login page.")