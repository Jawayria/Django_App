# Generated by Django 3.1 on 2020-08-31 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0009_auto_20200831_0738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='admin_id',
            new_name='admin',
        ),
    ]
