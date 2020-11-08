from django.contrib import admin
from .models import OpenRoom, PrivateRoom, PasswordProtectedRoom

# Register your models here.
admin.site.register(OpenRoom)
admin.site.register(PrivateRoom)
admin.site.register(PasswordProtectedRoom)

