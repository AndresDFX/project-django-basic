# Generated by Django 5.1.1 on 2024-09-19 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_pedido_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='producto',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
