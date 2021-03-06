# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-09 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('typeof', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('contact_num', models.CharField(max_length=150, null=True)),
                ('password', models.CharField(max_length=150)),
                ('salt', models.CharField(max_length=255)),
                ('picture', models.ImageField(default='user/default_profile.png', upload_to='user/%Y/%m/%d/')),
                ('billingAdd', models.CharField(max_length=1024)),
                ('shippingAdd', models.CharField(max_length=1024)),
            ],
        ),
    ]
