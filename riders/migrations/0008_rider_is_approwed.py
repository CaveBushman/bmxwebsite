# Generated by Django 3.0.5 on 2020-04-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0007_auto_20200416_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='is_approwed',
            field=models.BooleanField(default=False),
        ),
    ]
