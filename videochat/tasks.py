from django.utils.datetime_safe import datetime

from config import celery_app
from confirence_socket.views import sio
from videochat.models import OpenRoom


@celery_app.task
def check_room_availability():
    finished_rooms = OpenRoom.objects.filter(finish_time__lte=datetime.now())
    if finished_rooms.exists():
        finished_rooms.update(availible=False)
        for room in finished_rooms:
            sio.close_room(room.id)
