# Generated by Django 4.1 on 2022-09-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_order_product_alter_order_u_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.IntegerField(default=1),
        ),
    ]
