# Generated by Django 5.1 on 2024-08-15 08:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('PAYMENT', 'Payment'), ('FINE', 'Fine')], default='PAYMENT', max_length=24),
        ),
        migrations.AlterField(
            model_name='payment',
            name='session_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid')], default='PENDING', max_length=24),
        ),
    ]
