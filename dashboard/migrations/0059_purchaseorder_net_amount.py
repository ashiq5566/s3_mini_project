# Generated by Django 4.1.1 on 2022-10-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0058_remove_purchaseditems_item_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='net_amount',
            field=models.IntegerField(null=True),
        ),
    ]
