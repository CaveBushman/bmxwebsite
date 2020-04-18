# Generated by Django 3.0.5 on 2020-04-18 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20200418_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='charge',
        ),
        migrations.AddField(
            model_name='category',
            name='age_from',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='age_to',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Charge',
        ),
    ]
