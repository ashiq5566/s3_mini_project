# Generated by Django 4.1.1 on 2022-10-12 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0069_alter_purchaseorder_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseditems',
            name='total_amt',
            field=models.IntegerField(null=True),
        ),
    ]
