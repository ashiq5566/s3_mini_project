# Generated by Django 4.1.1 on 2022-10-20 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0079_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pending',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]