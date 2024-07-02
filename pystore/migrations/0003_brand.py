# Generated by Django 5.0.6 on 2024-07-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pystore', '0002_color_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='photos/')),
            ],
        ),
    ]
