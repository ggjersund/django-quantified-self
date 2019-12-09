# Generated by Django 3.0 on 2019-12-08 14:29

from django.db import migrations, models
import quantified_self.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('quantified_self', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intcountevent',
            name='uuid',
            field=models.UUIDField(default=quantified_self.mixins.generate_uuid, unique=True),
        ),
        migrations.AlterField(
            model_name='intervalevent',
            name='uuid',
            field=models.UUIDField(default=quantified_self.mixins.generate_uuid, unique=True),
        ),
    ]