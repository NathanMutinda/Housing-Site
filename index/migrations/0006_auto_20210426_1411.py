# Generated by Django 3.1.5 on 2021-04-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20210426_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='picture',
            field=models.ImageField(blank=True, default='cart.png', null=True, upload_to=''),
        ),
    ]
