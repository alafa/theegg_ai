# Generated by Django 3.1.4 on 2021-01-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20210111_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoitem',
            name='image_preview',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
