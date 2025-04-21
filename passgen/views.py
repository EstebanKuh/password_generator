from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(req):
    return HttpResponse('Home page')

def passgen(req):
    char = list('abcdefghijklmnopqrstuvwxyz')
    pwsd = ""
    for x in range(15):
        pwsd += random.choice(char)
    
    return JsonResponse({'password': pwsd})