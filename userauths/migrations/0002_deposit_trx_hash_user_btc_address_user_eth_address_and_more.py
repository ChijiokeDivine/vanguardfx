# Generated by Django 4.2.3 on 2023-12-23 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="deposit",
            name="trx_hash",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="btc_address",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="eth_address",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="usdt_address",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="withdraw",
            name="confirmed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="referral_code",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=10,
                max_length=20,
                prefix="profit",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="withdraw",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
