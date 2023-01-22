# Generated by Django 4.0.5 on 2023-01-22 22:45

import dish.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0005_historicaldish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(validators=[dish.models.validate_price], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(validators=[dish.models.validate_weight], verbose_name='Вес/количество (граммы)'),
        ),
        migrations.AlterField(
            model_name='historicaldish',
            name='price',
            field=models.IntegerField(validators=[dish.models.validate_price], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='historicaldish',
            name='weight',
            field=models.IntegerField(validators=[dish.models.validate_weight], verbose_name='Вес/количество (граммы)'),
        ),
    ]
