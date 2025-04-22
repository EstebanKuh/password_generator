from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(req):
    return render(req, 'home.html')

def passgen(req):
    char = list('abcdefghijklmnopqrstuvwxyz')
    if req.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if req.GET.get('digits'):
        char.extend(list('0123456789'))

    if req.GET.get('symbol'):
        char.extend(list('+-*/%&!@$~^'))

    length = int(req.GET.get('length', 10))

    pswd = ""
    for x in range(length):
        pswd += random.choice(char)
    
    return render(req, 'password.html',  {'pswd': pswd})