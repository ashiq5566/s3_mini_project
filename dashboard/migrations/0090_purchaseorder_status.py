# Generated by Django 4.1.1 on 2022-10-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0089_alter_purchaseorder_net_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
