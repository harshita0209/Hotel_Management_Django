# Generated by Django 3.2.4 on 2021-06-30 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comments', models.TextField(max_length=1000)),
                ('created_on', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
