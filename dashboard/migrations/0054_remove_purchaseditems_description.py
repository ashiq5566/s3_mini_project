# Generated by Django 4.1.1 on 2022-10-03 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0053_rename_item_purchaseditems_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseditems',
            name='description',
        ),
    ]
