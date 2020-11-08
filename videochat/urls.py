from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import room, room_list

urlpatterns = [
    path('room/', room_list, name='room-list'),
    path('room/<uuid:room_id>', room, name='room'),
]

urlpatterns += staticfiles_urlpatterns()