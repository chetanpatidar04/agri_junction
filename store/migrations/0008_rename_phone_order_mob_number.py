# Generated by Django 4.1 on 2022-09-09 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_address_order_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone',
            new_name='mob_number',
        ),
    ]
