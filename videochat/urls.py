from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from config import settings
from .views import room, room_list

urlpatterns = [
    path('room/', room_list, name='room-list'),
    path('room/<uuid:room_id>', room, name='room'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)