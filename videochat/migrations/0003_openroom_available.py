# Generated by Django 3.1.3 on 2020-11-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videochat', '0002_auto_20201103_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='openroom',
            name='available',
            field=models.BooleanField(default=True, editable=False, verbose_name='Комната активна'),
        ),
    ]
