# Generated by Django 4.1.1 on 2022-10-20 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0082_alter_payment_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='pending',
        ),
    ]
