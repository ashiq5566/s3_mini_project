# Generated by Django 4.1.1 on 2022-10-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0040_rename_cusomer_no_customer_customer_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_no',
            field=models.IntegerField(null=True),
        ),
    ]
