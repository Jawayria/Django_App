# Generated by Django 3.1 on 2020-08-27 10:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Contest', '0002_auto_20200827_1023'),
        ('Groups', '0002_auto_20200826_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]