# Generated by Django 3.1.4 on 2021-01-17 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20210117_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videoitem',
            old_name='url',
            new_name='youtube_id',
        ),
    ]