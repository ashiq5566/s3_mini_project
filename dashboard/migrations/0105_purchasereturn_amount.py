# Generated by Django 4.1.1 on 2022-10-31 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0104_purchasereturn_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasereturn',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]