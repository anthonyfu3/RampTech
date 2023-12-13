# Generated by Django 4.1.13 on 2023-12-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aircraft", "0004_alter_aircraftnote_aircraft_model_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aircraftnote",
            name="location",
            field=models.CharField(
                blank=True,
                choices=[
                    ("H1", "hanger_1"),
                    ("H2", "hanger_2"),
                    ("H3", "hanger_3"),
                    ("H4", "hanger_4"),
                    ("R1", "row_1"),
                    ("R2", "row_2"),
                    ("R3", "row_3"),
                    ("R4", "row_4"),
                    ("R5", "row_5"),
                    ("R6", "row_6"),
                    ("T-D", "tie_down"),
                    ("Gama", "gama"),
                    ("O-R", "off_ramp"),
                    ("Cstm", "customs"),
                    ("NJ", "netjets"),
                ],
                max_length=30,
                null=True,
            ),
        ),
    ]
