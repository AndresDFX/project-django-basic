# Generated by Django 5.1.1 on 2024-09-19 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='nombre_pedido',
            field=models.CharField(default='hola', max_length=30),
            preserve_default=False,
        ),
    ]
