# Generated by Django 4.2.5 on 2024-09-01 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0006_alter_games_p1_alter_games_p2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='p1',
        ),
        migrations.RemoveField(
            model_name='games',
            name='p2',
        ),
        migrations.RemoveField(
            model_name='games',
            name='player',
        ),
        migrations.AddField(
            model_name='games',
            name='player1',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player1', to='RestAPI.players'),
        ),
        migrations.AddField(
            model_name='games',
            name='player2',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player2', to='RestAPI.players'),
        ),
        migrations.AddField(
            model_name='games',
            name='split',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='games',
            name='tournament',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='RestAPI.tournament'),
        ),
        migrations.AddField(
            model_name='games',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sections',
            name='tournament',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='RestAPI.tournament'),
        ),
    ]
