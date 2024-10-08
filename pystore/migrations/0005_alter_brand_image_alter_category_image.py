# Generated by Django 5.0.6 on 2024-07-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pystore', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, upload_to='brand_photos/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='cat_photos/'),
        ),
    ]
