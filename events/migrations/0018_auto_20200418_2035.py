# Generated by Django 3.0.5 on 2020-04-18 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20200418_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_type',
            new_name='type',
        ),
    ]
