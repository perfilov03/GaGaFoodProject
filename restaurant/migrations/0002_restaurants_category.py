# Generated by Django 4.0.5 on 2022-06-25 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='category',
            field=models.TextField(null=True, verbose_name='Категория ресторана'),
        ),
    ]
