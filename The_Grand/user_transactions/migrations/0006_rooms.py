# Generated by Django 3.2.4 on 2021-07-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_transactions', '0005_alter_reviews_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room_type', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
