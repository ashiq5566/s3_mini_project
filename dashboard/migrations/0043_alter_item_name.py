# Generated by Django 4.1.1 on 2022-10-02 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0042_alter_item_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]