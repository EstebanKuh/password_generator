from django.shortcuts import render, HttpResponse
import string
import secrets

# Create your views here.
def home(req):
    return render(req, 'home.html')

def passgen(req):
    char = list(string.ascii_lowercase)
    if req.GET.get('uppercase'):
        char.extend(list(string.ascii_uppercase))

    if req.GET.get('digits'):
        char.extend(list(string.digits))

    if req.GET.get('symbol'):
        char.extend(list('+-*/%&!@$~^'))

    length = int(req.GET.get('length', 10))
    if length <= 0:
        return HttpResponse("Longitud debe ser un número positivo")

    pswd = ''.join(secrets.choice(char) for _ in range(length))
    
    return render(req, 'password.html',  {'pswd': pswd})