# Generated by Django 4.1.3 on 2022-11-07 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_datetime_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categories',
            field=models.ManyToManyField(related_name='Category', to='blog.category'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_released',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 17, 56, 6, 744983, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='Posts', to='blog.category'),
        ),
    ]
