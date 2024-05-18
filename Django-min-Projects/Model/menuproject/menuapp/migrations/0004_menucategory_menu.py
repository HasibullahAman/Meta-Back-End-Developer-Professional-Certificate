# Generated by Django 5.0.1 on 2024-05-14 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0003_rename_course_menuitems_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='menuapp.menucategory')),
            ],
        ),
    ]