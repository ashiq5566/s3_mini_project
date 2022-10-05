# Generated by Django 4.1.1 on 2022-10-01 11:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_item_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]