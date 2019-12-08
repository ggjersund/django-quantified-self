# Generated by Django 3.0 on 2019-12-08 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntCountEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True)),
                ('label', models.CharField(blank=True, default='', max_length=50)),
                ('score', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value has to be greater or equal to zero.'), django.core.validators.MaxValueValidator(10, 'Value has to be less or equal to 10.')])),
                ('datetime', models.DateTimeField()),
                ('value', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'integer count event',
                'verbose_name_plural': 'integer count events',
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='IntervalEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True)),
                ('label', models.CharField(blank=True, default='', max_length=50)),
                ('score', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value has to be greater or equal to zero.'), django.core.validators.MaxValueValidator(10, 'Value has to be less or equal to 10.')])),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'interval event',
                'verbose_name_plural': 'interval events',
                'ordering': ['-start'],
            },
        ),
    ]
