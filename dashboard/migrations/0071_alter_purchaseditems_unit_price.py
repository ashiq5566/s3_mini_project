# Generated by Django 4.1.1 on 2022-10-12 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0070_purchaseditems_total_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseditems',
            name='unit_price',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
