# Generated by Django 2.2 on 2020-11-13 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Groups', '0001_initial'),
        ('Contest', '0002_auto_20201113_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contest.League'),
        ),
        migrations.AddField(
            model_name='league',
            name='groups',
            field=models.ManyToManyField(blank=True, to='Groups.Group'),
        ),
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together={('user', 'group', 'match')},
        ),
    ]