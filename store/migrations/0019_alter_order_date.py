# Generated by Django 4.1 on 2022-09-15 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_order_status_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 11, 4, 4, 481570)),
        ),
    ]
