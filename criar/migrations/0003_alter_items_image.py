# Generated by Django 4.1.5 on 2023-01-28 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criar', '0002_alter_items_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]