# Generated by Django 3.0.5 on 2020-04-18 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20200418_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='charge_online',
        ),
        migrations.RemoveField(
            model_name='category',
            name='charge_onspot',
        ),
        migrations.CreateModel(
            name='EventCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_online', models.IntegerField()),
                ('charge_onspot', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventType')),
            ],
        ),
    ]
