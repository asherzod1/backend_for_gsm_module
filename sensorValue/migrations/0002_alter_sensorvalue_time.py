# Generated by Django 4.2 on 2023-04-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorValue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorvalue',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
