from django.shortcuts import render
from .models import OpenRoom

# Create your views here.
def room(request, room_id):
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