# Generated by Django 3.0.5 on 2020-04-19 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0016_rider_have_valid_licence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rider',
            old_name='date_of_birthday',
            new_name='date_of_birth',
        ),
    ]
