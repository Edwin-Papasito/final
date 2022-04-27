# Generated by Django 3.2.5 on 2022-04-25 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicaciones', '0036_perfil_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=6)),
                ('modelo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('foto_v', models.ImageField(null=True, upload_to='vehiculos')),
                ('foto_tarjeta', models.ImageField(null=True, upload_to='propiedad')),
                ('aprobado', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion_inicio', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc_ini', models.CharField(max_length=10)),
                ('numero_ini', models.CharField(max_length=10)),
                ('extra_ini', models.CharField(max_length=100)),
                ('direccion_2', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc_2', models.CharField(max_length=10)),
                ('numero_2', models.CharField(max_length=10)),
                ('extra_2', models.CharField(max_length=100)),
                ('direccion_3', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc_3', models.CharField(max_length=10)),
                ('numero_3', models.CharField(max_length=10)),
                ('extra_3', models.CharField(max_length=100)),
                ('direccion_4', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc_4', models.CharField(max_length=10)),
                ('numero_4', models.CharField(max_length=10)),
                ('extra_4', models.CharField(max_length=100)),
                ('direccion_fin', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc_fin', models.CharField(max_length=10)),
                ('numero_fin', models.CharField(max_length=10)),
                ('extra_fin', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Auto',
        ),
        migrations.DeleteModel(
            name='Direccion2',
        ),
    ]
