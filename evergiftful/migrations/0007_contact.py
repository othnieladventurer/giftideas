# Generated by Django 5.0.1 on 2024-01-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evergiftful', '0006_product_wishlist_alter_wishlist_products_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
