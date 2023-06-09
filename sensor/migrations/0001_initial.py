# Generated by Django 4.2 on 2023-04-05 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='building.building')),
            ],
        ),
    ]
