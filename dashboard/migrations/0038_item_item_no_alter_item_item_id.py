# Generated by Django 4.1.1 on 2022-10-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0037_remove_myuuidmodel_id_alter_myuuidmodel_regnumber1'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
