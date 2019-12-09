# Generated by Django 3.0 on 2019-12-08 14:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quantified_self', '0002_auto_20191208_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intcountevent',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='intervalevent',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]