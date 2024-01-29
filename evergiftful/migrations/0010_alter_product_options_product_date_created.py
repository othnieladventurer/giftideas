# Generated by Django 5.0.1 on 2024-01-28 21:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evergiftful', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
