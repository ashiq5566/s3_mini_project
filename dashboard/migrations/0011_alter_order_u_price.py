# Generated by Django 4.1 on 2022-09-07 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_order_u_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='u_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productunitprice', to='dashboard.product'),
        ),
    ]
