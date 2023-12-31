# Generated by Django 4.1.13 on 2023-12-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aircraft", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aircraftnote",
            name="transportation_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("none", "None"),
                    ("driver", "Driver"),
                    ("rental", "Rental"),
                    ("self-park", "Self-Park"),
                    ("Ride Share", "Ride Share"),
                ],
                max_length=10,
                null=True,
            ),
        ),
    ]
