# Generated by Django 5.1.1 on 2024-09-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_custom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
