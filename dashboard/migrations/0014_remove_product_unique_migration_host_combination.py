# Generated by Django 4.1 on 2022-09-07 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_order_u_price_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='product',
            name='unique_migration_host_combination',
        ),
    ]
