# Generated by Django 4.1.1 on 2022-10-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0083_remove_payment_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='pending',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
