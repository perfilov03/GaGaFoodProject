# Generated by Django 4.0.5 on 2022-06-26 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_restaurants_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории ресторанов'},
        ),
        migrations.AlterModelOptions(
            name='restaurants',
            options={'ordering': ['title'], 'verbose_name': 'Ресторан', 'verbose_name_plural': 'Рестораны'},
        ),
    ]
