# Generated by Django 3.1 on 2020-09-04 05:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Groups', '0010_auto_20200831_1534'),
        ('Contest', '0003_auto_20200831_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together={('user_id', 'group_id', 'match_id')},
        ),
    ]
