# Generated by Django 4.2.11 on 2024-06-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="content",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
