# Generated by Django 4.2 on 2023-04-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_products_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
