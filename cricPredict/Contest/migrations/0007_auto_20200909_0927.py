# Generated by Django 3.1 on 2020-09-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contest', '0006_auto_20200909_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='match_type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Quarter Final', 'Quarter Final'), ('Semi Final', 'Semi Final'), ('Play-off', 'Play-off'), ('Final', 'Final')], max_length=50),
        ),
    ]
