# Generated by Django 4.2.11 on 2024-08-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "payment",
            "0007_alter_payment_payment_type_alter_payment_session_url_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="session_url",
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]
