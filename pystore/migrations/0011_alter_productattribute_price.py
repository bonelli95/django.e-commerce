# Generated by Django 5.0.6 on 2024-07-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pystore', '0010_alter_size_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
