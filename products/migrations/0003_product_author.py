# Generated by Django 3.2.7 on 2021-09-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
