# Generated by Django 4.0.6 on 2022-07-23 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo_status',
            options={'verbose_name': 'status', 'verbose_name_plural': 'Status'},
        ),
    ]
