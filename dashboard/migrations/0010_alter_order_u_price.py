# Generated by Django 4.1 on 2022-09-07 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_product_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_units', to='dashboard.product'),
        ),
    ]
