# Generated by Django 4.1 on 2022-09-20 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pack_size',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 11, 37, 4, 392268)),
        ),
    ]
