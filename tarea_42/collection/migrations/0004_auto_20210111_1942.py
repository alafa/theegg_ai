# Generated by Django 3.1.4 on 2021-01-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_videoitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoitem',
            name='category',
            field=models.IntegerField(choices=[(0, 'Música'), (1, 'Cine'), (2, 'Animales'), (3, 'Ciencia'), (4, 'Otros')], default=0, max_length=32),
        ),
    ]
