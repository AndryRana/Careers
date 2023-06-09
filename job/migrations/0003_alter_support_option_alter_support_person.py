# Generated by Django 4.1.5 on 2023-02-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0002_support"),
    ]

    operations = [
        migrations.AlterField(
            model_name="support",
            name="option",
            field=models.CharField(
                choices=[
                    ("Wanted to update my resume", "Wanted to update my resume"),
                    ("Others", "Others"),
                    ("I forgot my Password", "I forgot my Password"),
                    ("I forgot my account", "I forgot my account"),
                ],
                max_length=60,
            ),
        ),
        migrations.AlterField(
            model_name="support",
            name="person",
            field=models.CharField(
                choices=[("Candidate", "Candidate"), ("Employee", "Employee")],
                max_length=60,
            ),
        ),
    ]
