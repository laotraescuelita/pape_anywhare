# Generated by Django 4.1.7 on 2023-03-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pape', '0009_alter_producto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='novedad',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
