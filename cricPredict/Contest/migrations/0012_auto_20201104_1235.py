# Generated by Django 3.1 on 2020-11-04 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contest', '0011_league_api_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='api_id',
            new_name='league_id',
        ),
    ]