# Generated by Django 4.2.3 on 2024-01-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0003_transaction_plan_interval_processed_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transaction",
            options={"verbose_name_plural": "Users that invested"},
        ),
        migrations.AddField(
            model_name="transaction",
            name="interval_count",
            field=models.IntegerField(default=0),
        ),
    ]
