# Generated by Django 3.0.5 on 2020-04-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20200416_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('MČR', 'MČR'), ('ČP', 'ČP'), ('ČL', 'ČL'), ('ML', 'ML'), ('V', 'V')], default='ML', max_length=10),
            preserve_default=False,
        ),
    ]