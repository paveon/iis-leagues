# Generated by Django 2.1.1 on 2018-10-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_auto_20181004_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='sponsors',
            field=models.ManyToManyField(blank=True, through='leagues.Sponsorship', to='leagues.Sponsor'),
        ),
    ]