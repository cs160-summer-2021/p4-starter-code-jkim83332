# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def interactive_user(request):
    return render(request, 'draw/interactive-user.html')

def interactive_user_2(request):
    return render(request, 'draw/interactive-user-2.html')

def interactive_big(request):
    return render(request, 'draw/interactive-big.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
