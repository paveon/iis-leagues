# Generated by Django 2.1.1 on 2018-11-18 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0021_auto_20181118_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='duration of the match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='matches_won', to='leagues.Team', verbose_name='winning team'),
        ),
    ]
