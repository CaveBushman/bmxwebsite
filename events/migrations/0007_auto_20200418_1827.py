# Generated by Django 3.0.5 on 2020-04-18 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_event_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_type',
            new_name='type',
        ),
    ]