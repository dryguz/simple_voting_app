# Generated by Django 4.1.6 on 2023-02-05 15:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="questions",
            old_name="question_test",
            new_name="question_text",
        ),
    ]
