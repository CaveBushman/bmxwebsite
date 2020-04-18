# Generated by Django 3.0.5 on 2020-04-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_remove_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='label',
            field=models.CharField(choices=[('MCR', 'MCR'), ('CP', 'CP'), ('CL', 'CL'), ('ML', 'ML'), ('V', 'V')], default='CP', max_length=10),
            preserve_default=False,
        ),
    ]