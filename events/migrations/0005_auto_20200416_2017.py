# Generated by Django 3.0.5 on 2020-04-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200416_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='ranking_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
