from django.urls import path

from videochat.views import room, room_list, home

urlpatterns = [
    path('', home, name='home'),
    path('room/', room_list, name='room-list'),
    path('room/<uuid:room_id>', room, name='room'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += staticfiles_urlpatterns()
