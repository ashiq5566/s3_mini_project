# Generated by Django 4.1.1 on 2022-10-20 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0078_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]