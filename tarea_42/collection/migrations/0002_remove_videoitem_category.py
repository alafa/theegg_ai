# Generated by Django 3.1.4 on 2021-01-11 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoitem',
            name='category',
        ),
    ]