# Generated by Django 3.2.5 on 2022-04-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0029_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion_fin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=10)),
                ('extra', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion_inicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(choices=[('Calle', 'Cl'), ('Carrera', 'Cra'), ('Diagonal', 'Dg'), ('Transversal', 'Tr'), ('Avenida', 'Av')], default='Cl', max_length=11)),
                ('cc', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=10)),
                ('extra', models.CharField(max_length=100)),
            ],
        ),
    ]