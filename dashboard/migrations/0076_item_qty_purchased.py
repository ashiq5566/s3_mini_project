# Generated by Django 4.1.1 on 2022-10-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0075_alter_purchaseorder_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='qty_purchased',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
