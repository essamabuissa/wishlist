# Generated by Django 3.0.3 on 2020-02-20 08:41

from django.db import migrations, models
import wish_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0003_auto_20200220_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUID',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name=wish_app.models.Item)),
            ],
        ),
    ]
