# Generated by Django 4.1.3 on 2023-06-18 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]