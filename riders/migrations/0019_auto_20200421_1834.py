# Generated by Django 3.0.5 on 2020-04-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0018_auto_20200420_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='nationality',
            field=models.CharField(default='CZE', max_length=3),
        ),
        migrations.AlterField(
            model_name='rider',
            name='gender',
            field=models.CharField(choices=[('Muž/Male', 'Muž/Male'), ('Žena/Female', 'Žena/Female'), ('Ostatní/Other', 'Ostatní/Other')], default='Muž/Male', max_length=50),
        ),
    ]