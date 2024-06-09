# Generated by Django 5.0.1 on 2024-05-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(blank=True, max_length=300)),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]