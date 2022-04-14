# Generated by Django 3.2.5 on 2022-04-14 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='apellido',
            field=models.CharField(max_length=50, null=True, verbose_name='apellido'),
        ),
        migrations.AddField(
            model_name='user',
            name='cedula',
            field=models.CharField(max_length=10, null=True, verbose_name='cedula'),
        ),
        migrations.AddField(
            model_name='user',
            name='certificado',
            field=models.ImageField(null=True, upload_to='certificados'),
        ),
        migrations.AddField(
            model_name='user',
            name='direccion',
            field=models.CharField(max_length=150, null=True, verbose_name='direccion'),
        ),
        migrations.AddField(
            model_name='user',
            name='foto',
            field=models.ImageField(null=True, upload_to='Fotografias'),
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=10, null=True, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, verbose_name='nombre'),
        ),
    ]