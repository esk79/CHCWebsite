# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-13 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('title', models.CharField(max_length=125)),
                ('facebook', models.CharField(max_length=125)),
                ('linkedin', models.CharField(max_length=125)),
                ('github', models.CharField(max_length=125)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
