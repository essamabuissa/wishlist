# Generated by Django 3.0.3 on 2020-02-20 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0004_myuuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='Items_images', width_field=200),
        ),
    ]