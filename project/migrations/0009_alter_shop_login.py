# Generated by Django 5.0.1 on 2024-01-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_shop_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='login',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
