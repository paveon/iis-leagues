# Generated by Django 2.1.1 on 2018-11-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0017_auto_20181116_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]