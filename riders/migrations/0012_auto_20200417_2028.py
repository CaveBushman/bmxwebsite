# Generated by Django 3.0.5 on 2020-04-17 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0011_auto_20200417_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rider',
            old_name='surname',
            new_name='last_name',
        ),
    ]
