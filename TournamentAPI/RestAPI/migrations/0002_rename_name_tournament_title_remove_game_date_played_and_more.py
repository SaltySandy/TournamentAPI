# Generated by Django 4.2.5 on 2024-09-01 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='game',
            name='date_played',
        ),
        migrations.RemoveField(
            model_name='game',
            name='player_black',
        ),
        migrations.RemoveField(
            model_name='game',
            name='player_white',
        ),
        migrations.RemoveField(
            model_name='game',
            name='round',
        ),
        migrations.RemoveField(
            model_name='game',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='player',
            name='section',
        ),
        migrations.RemoveField(
            model_name='player',
            name='see_td_flag',
        ),
        migrations.RemoveField(
            model_name='player',
            name='state',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.RemoveField(
            model_name='player',
            name='uscf_expiration',
        ),
        migrations.AddField(
            model_name='game',
            name='board',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='game',
            name='color1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='color2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='p1',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='player1_tournaments', to='RestAPI.tournament'),
        ),
        migrations.AddField(
            model_name='game',
            name='p2',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='player2_tournaments', to='RestAPI.tournament'),
        ),
        migrations.AddField(
            model_name='game',
            name='r1',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='game',
            name='r2',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='player',
            name='base',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='player',
            name='tnmt',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='game',
            name='result',
            field=models.FloatField(default=99),
        ),
    ]
