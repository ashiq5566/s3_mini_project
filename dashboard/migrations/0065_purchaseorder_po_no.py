# Generated by Django 4.1.1 on 2022-10-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0064_remove_purchaseditems_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='po_no',
            field=models.IntegerField(null=True),
        ),
    ]