from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

import uuid

# Create your models here.
class OpenRoom(models.Model):

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    speaker = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Спикер')
    start_time = models.DateTimeField('Время начала')
    finish_time = models.DateTimeField('Время окончания')

    def get_absolute_url(self):
        return reverse_lazy('room', args=[self.id])

    def __str__(self):
        return 'Комната №{}'.format(self.id)

    class Meta:
        verbose_name = 'открытая комната'

class PrivateRoom(OpenRoom):
    
    users = models.ManyToManyField(to=User)

    class Meta:
        verbose_name = 'личная комната'

class PasswordProtectedRoom(OpenRoom):

    password = models.CharField(verbose_name='Пароль комнаты', max_length=32)

    class Meta:
        verbose_name = 'комната с паролем'
