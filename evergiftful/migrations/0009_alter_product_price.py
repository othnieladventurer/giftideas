# Generated by Django 5.0.1 on 2024-01-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evergiftful', '0008_contact_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
