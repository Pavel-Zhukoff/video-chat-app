from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import OpenRoom, PasswordProtectedRoom, PrivateRoom


# Create your views here.
def get_room_model_object(room_id):
    """ return room model object by room_id """
    if PasswordProtectedRoom.objects.filter(id=room_id).exists():
        return PasswordProtectedRoom.objects.get(id=room_id)
    elif PrivateRoom.objects.filter(id=room_id).exists():
        return PrivateRoom.objects.get(id=room_id)
    elif OpenRoom.objects.filter(id=room_id).exists():
        return OpenRoom.objects.get(id=room_id)

    return None

def room(request, room_id):
    room = get_room_model_object(room_id)
    if room is None: return HttpResponse('404. Room not found.')
    print(room)
    return render(request, 'room.html', {
        'title': 'Комната №{}'.format(room_id), 
        'room': OpenRoom.objects.get(id=room_id),
    })


def room_list(request):
    rooms = OpenRoom.objects.all()
    return render(request, 'room_list.html', {
        'title': 'Список комнат',
        'rooms': rooms,
    })


def home(request):

    return render(request, 'home.html', {
        'title': 'Главная',
    })