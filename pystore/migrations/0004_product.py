# Generated by Django 5.0.6 on 2024-07-02 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pystore', '0003_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='product_photos/')),
                ('slug', models.CharField(max_length=250)),
                ('detail', models.TextField()),
                ('specification', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pystore.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pystore.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pystore.color')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pystore.size')),
            ],
        ),
    ]
