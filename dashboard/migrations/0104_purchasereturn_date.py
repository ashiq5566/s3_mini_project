# Generated by Django 4.1.1 on 2022-10-31 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0103_rename_item_id_purchasereturn_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasereturn',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]