# Generated by Django 4.0.6 on 2022-07-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_todo_status_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_list',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Pending', 'Pending')], default=None, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='todo_status',
        ),
    ]