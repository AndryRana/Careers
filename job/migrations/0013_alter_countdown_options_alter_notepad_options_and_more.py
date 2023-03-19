# Generated by Django 4.1.5 on 2023-03-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0012_alter_message_situation_alter_support_option_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="countdown",
            options={"verbose_name_plural": "Countdown"},
        ),
        migrations.AlterModelOptions(
            name="notepad",
            options={"verbose_name_plural": "Notepad"},
        ),
        migrations.AlterModelOptions(
            name="openings",
            options={"verbose_name_plural": "Openings"},
        ),
        migrations.AlterModelOptions(
            name="registered_email",
            options={"verbose_name_plural": "Registered"},
        ),
        migrations.AlterModelOptions(
            name="support",
            options={"verbose_name_plural": "Support"},
        ),
        migrations.AlterModelOptions(
            name="waitinglist",
            options={"verbose_name_plural": "Waiting list"},
        ),
        migrations.AlterField(
            model_name="support",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="support",
            name="option",
            field=models.CharField(
                choices=[
                    ("Others", "Others"),
                    ("Wanted to update my resume", "Wanted to update my resume"),
                    ("I forgot my Password", "I forgot my Password"),
                    ("I forgot my account", "I forgot my account"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="support",
            name="situation",
            field=models.CharField(
                choices=[("Pending", "Pending"), ("Done", "Done")],
                default="Pending",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="waitinglist",
            name="email",
            field=models.EmailField(max_length=150),
        ),
    ]
