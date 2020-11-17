import os

import socketio

from config import settings
from videochat.models import OpenRoom

if settings.DEBUG:
    sio = socketio.Server(logger=True, ngineio_logger=True, async_mode='eventlet')
else:
    sio = socketio.Server(async_mode='eventlet')

basedir = os.path.dirname(os.path.realpath(__file__))


@sio.event
def connect(sid, environ):
    pass


@sio.on('join-room')
def join_room(sid, room_id, user_peer_id):
    if OpenRoom.objects.filter(id=room_id, available=True).exists():
        sio.enter_room(sid, room_id)
        sio.save_session(sid , {'room_id': room_id, 'peer_id': user_peer_id})
        sio.emit('user-connected', user_peer_id, room=room_id, skip_sid=sid)
    else:
        sio.close_room(room_id)


@sio.event
def disconnect(sid):
    session = sio.get_session(sid)
    sio.emit('user-disconnected', session['peer_id'], room=session['room_id'], skip_sid=sid)



#web: gunicorn -b 0.0.0.0:5000 --worker-class eventlet -w 1 server:app
#web: python server.py
#5000 port
# port = int(os.environ.get("PORT", 5000))
# eventlet.wsgi.server(eventlet.listen(('0.0.0.0', port)), run_server())
