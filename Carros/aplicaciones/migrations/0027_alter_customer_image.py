# Generated by Django 3.2.5 on 2022-04-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0026_auto_20220415_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='autos'),
        ),
    ]