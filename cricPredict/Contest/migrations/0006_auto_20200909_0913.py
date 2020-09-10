# Generated by Django 3.1 on 2020-09-09 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contest', '0005_auto_20200909_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='score',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Contest.score'),
        ),
        migrations.AlterField(
            model_name='score',
            name='match_type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Quarter Final', 'Quarter Final'), ('Semi Final', 'Semi Final'), ('Playoff', 'PlayOff'), ('Final', 'Final')], max_length=50),
        ),
        migrations.AlterField(
            model_name='score',
            name='result',
            field=models.CharField(choices=[('Win', 'Win'), ('Lose', 'Lose'), ('Draw', 'Draw')], max_length=20),
        ),
    ]