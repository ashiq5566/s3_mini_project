# Generated by Django 4.1.1 on 2022-10-25 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0092_remove_purchaseditems_item_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseditems',
            name='item_name',
        ),
        migrations.AddField(
            model_name='purchaseditems',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.item'),
        ),
    ]
