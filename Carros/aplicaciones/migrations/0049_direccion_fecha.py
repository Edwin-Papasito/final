# Generated by Django 3.2.5 on 2022-05-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0048_auto_20220429_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha'),
        ),
    ]
