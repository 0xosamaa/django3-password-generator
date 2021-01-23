from django.shortcuts import render
import random

# Create your views here.


def home(request):

    return render(request, 'generator/home.html', {'range': range(6,31)})


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})

