# Generated by Django 3.0.5 on 2020-04-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0017_auto_20200419_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='is_valid_transponder_20',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rider',
            name='is_valid_transponder_24',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rider',
            name='is_valid_transponder_mtb',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rider',
            name='is_valid_transponder_other',
            field=models.BooleanField(default=True),
        ),
    ]
