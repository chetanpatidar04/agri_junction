# Generated by Django 4.1 on 2022-09-11 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 11, 55, 3, 279546)),
        ),
    ]
