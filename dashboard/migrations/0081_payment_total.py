# Generated by Django 4.1.1 on 2022-10-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0080_alter_payment_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='total',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
