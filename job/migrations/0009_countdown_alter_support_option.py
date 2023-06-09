# Generated by Django 4.1.5 on 2023-03-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0008_openings_alter_support_option_alter_support_person"),
    ]

    operations = [
        migrations.CreateModel(
            name="Countdown",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("timer", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="support",
            name="option",
            field=models.CharField(
                choices=[
                    ("I forgot my account", "I forgot my account"),
                    ("Wanted to update my resume", "Wanted to update my resume"),
                    ("I forgot my Password", "I forgot my Password"),
                    ("Others", "Others"),
                ],
                max_length=50,
            ),
        ),
    ]
