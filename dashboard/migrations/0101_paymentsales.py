# Generated by Django 4.1.1 on 2022-10-31 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0100_salesorder_solditems'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_no', models.IntegerField(null=True)),
                ('payment_id', models.CharField(max_length=100, null=True, unique=True)),
                ('paid', models.PositiveIntegerField(default=0, null=True)),
                ('total', models.PositiveIntegerField(null=True)),
                ('pending', models.PositiveIntegerField(default=0, null=True)),
                ('so_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.salesorder')),
            ],
        ),
    ]
