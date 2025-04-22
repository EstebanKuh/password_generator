from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(req):
    return render(req, 'home.html')

def passgen(req):
    char = list('abcdefghijklmnopqrstuvwxyz')
    pswd = ""
    for x in range(15):
        pswd += random.choice(char)
    
    return render(req, 'password.html',  {'pswd': pswd})