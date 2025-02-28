# Generated by Django 4.2.14 on 2024-07-12 03:35

from django.db import migrations, models
import importer.validators


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataimportsession',
            name='field_overrides',
            field=models.JSONField(blank=True, null=True, validators=[importer.validators.validate_field_defaults], verbose_name='Field Overrides'),
        ),
    ]
