# Generated by Django 4.2.6 on 2023-10-24 20:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0045_remove_scratch_preset"),
    ]

    operations = [
        migrations.RenameField(
            model_name="scratch",
            old_name="preset_fk",
            new_name="preset",
        ),
    ]