# Generated by Django 4.1.1 on 2022-10-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0068_remove_purchaseorder_generated_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
