# Generated by Django 4.1.1 on 2022-10-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0057_purchaseditems_item_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseditems',
            name='item_name',
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.IntegerField(null=True),
        ),
    ]
