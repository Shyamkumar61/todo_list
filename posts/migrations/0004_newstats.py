# Generated by Django 4.0.6 on 2022-07-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_todo_list_status_delete_todo_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='newstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.IntegerField()),
                ('mac', models.IntegerField()),
                ('iph', models.IntegerField()),
                ('android', models.IntegerField()),
                ('oth', models.IntegerField()),
            ],
            options={
                'verbose_name': 'NewStats',
            },
        ),
    ]
