# Generated by Django 2.1.1 on 2018-11-10 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0009_auto_20181107_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playedmatch',
            name='game_won',
        ),
        migrations.AddField(
            model_name='playedmatch',
            name='team',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='leagues.Team'),
            preserve_default=False,
        ),
    ]
