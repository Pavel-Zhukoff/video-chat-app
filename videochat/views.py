from enum import Enum

from django.http import HttpResponse
from django.shortcuts import render

from videochat.forms import PasswordRoomEnterForm
from .models import OpenRoom, PasswordProtectedRoom, PrivateRoom


class RoomType(Enum):
    PASSWORD_PROTECTED = 1
    PRIVATE = 2
    OPEN = 3


# Create your views here.
def get_room_model_object(room_id):
    """ return room with its type by room_id """

    if PasswordProtectedRoom.objects.filter(id=room_id).exists():
        return {'room': PasswordProtectedRoom.objects.get(id=room_id), 'type': RoomType.PASSWORD_PROTECTED}
    elif PrivateRoom.objects.filter(id=room_id).exists():
        return {'room': PrivateRoom.objects.get(id=room_id), 'type': RoomType.PRIVATE}
    elif OpenRoom.objects.filter(id=room_id).exists():
        return {'room': OpenRoom.objects.get(id=room_id), 'type': RoomType.PRIVATE}
    return None


def room(request, room_id):
    room = get_room_model_object(room_id)
    if room is None: return HttpResponse('404. Room not found.')
    if room.get('type') is RoomType.PASSWORD_PROTECTED:
        form = PasswordRoomEnterForm(request.POST)
        if request.method == "POST":
            if form.is_valid() and form.cleaned_data['password'] == room['room'].password:
                request.session['authed'] = True
            else:
                form.errors['password'] = ['Неверный пароль']
        if not request.session.get('authed', False):
            return render(request, 'room_password.html', {
                'title': 'Введите пароль от комнаты!',
                'form': form,
                'room': room['room'],
            })
    elif room.get('type') is RoomType.PRIVATE:
        if request.user not in room['room'].users.all() \
                and request.user != room['room'].speaker \
                and not request.user.is_authenticated:
            return render(request, 'room_restricted.html', {
                'title': 'Доступ запрещен!'
            })

    return render(request, 'room.html', {
        'title': 'Комната №{}'.format(room_id),
        'room': room['room'],
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