# Generated by Django 4.1.1 on 2022-10-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_item_item_no_alter_item_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cusomer_no',
            field=models.IntegerField(null=True),
        ),
    ]
