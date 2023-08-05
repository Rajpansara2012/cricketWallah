# Generated by Django 4.1.7 on 2023-03-30 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='livematch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname1', models.CharField(max_length=40)),
                ('teamname2', models.CharField(max_length=40)),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('wicket1', models.IntegerField(default=0)),
                ('wicket2', models.IntegerField(default=0)),
                ('over1', models.FloatField(default=0)),
                ('over2', models.FloatField(default=0)),
                ('balls', models.IntegerField(default=120)),
                ('win', models.IntegerField(default=0)),
                ('current_ball', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playername', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('ball', models.IntegerField(default=0)),
                ('wicket', models.IntegerField(default=0)),
                ('brun', models.IntegerField(default=0)),
                ('overs', models.FloatField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.team')),
            ],
        ),
        migrations.CreateModel(
            name='match_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('over', models.IntegerField(default=20)),
                ('venue', models.CharField(max_length=100)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.livematch')),
            ],
        ),
        migrations.AddField(
            model_name='livematch',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricket.team'),
        ),
    ]