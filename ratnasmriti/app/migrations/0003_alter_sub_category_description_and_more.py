# Generated by Django 5.0.4 on 2024-05-29 15:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_sub_category_description_sub_category_discount_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_category',
            name='Description',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='product_information',
            field=ckeditor.fields.RichTextField(),
        ),
    ]