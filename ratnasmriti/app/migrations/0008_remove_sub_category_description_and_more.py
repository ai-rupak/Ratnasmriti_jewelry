# Generated by Django 5.0.4 on 2024-05-29 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_category',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='product_information',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='product_name',
        ),
    ]