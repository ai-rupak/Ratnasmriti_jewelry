# Generated by Django 5.0.4 on 2024-05-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_sub_category_description_sub_category_discount_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='post',
            name='discouted_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]