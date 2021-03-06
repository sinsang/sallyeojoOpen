# Generated by Django 3.2.5 on 2021-07-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('team', models.IntegerField()),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'player',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiredRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('season_team', models.IntegerField()),
                ('g', models.IntegerField(db_column='G')),
                ('ip', models.CharField(db_column='IP', max_length=20)),
                ('startg', models.IntegerField(db_column='startG')),
                ('tired_score', models.FloatField()),
                ('pitcher_type', models.IntegerField()),
            ],
            options={
                'db_table': 'tired_record',
                'managed': False,
            },
        ),
    ]
