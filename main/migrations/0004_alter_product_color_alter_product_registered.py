# Generated by Django 4.1.3 on 2022-11-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_color_product_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='registered',
            field=models.BooleanField(),
        ),
    ]
