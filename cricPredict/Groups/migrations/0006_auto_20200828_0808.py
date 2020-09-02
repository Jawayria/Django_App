# Generated by Django 3.1 on 2020-08-28 08:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Groups', '0005_auto_20200828_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='privacy',
            field=models.CharField(choices=[('PB', 'public'), ('PR', 'private')], default='PR', max_length=10),
        ),
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
