# Generated by Django 3.2.5 on 2022-04-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0006_alter_user_certificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='direccion',
            field=models.CharField(max_length=150, null=True, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(null=True, upload_to='Fotografias'),
        ),
    ]
