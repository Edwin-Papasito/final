# Generated by Django 3.2.5 on 2022-04-15 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0023_delete_automovil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='foto_tarjeta',
        ),
        migrations.RemoveField(
            model_name='auto',
            name='foto_v',
        ),
    ]
