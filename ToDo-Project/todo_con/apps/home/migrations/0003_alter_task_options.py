# Generated by Django 3.2.6 on 2022-08-19 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('start_time', 'end_time')},
        ),
    ]
