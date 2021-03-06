# Generated by Django 4.0.5 on 2022-06-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cover', models.ImageField(upload_to='dish', verbose_name='Фотография')),
                ('weight', models.IntegerField(verbose_name='Вес/количество (граммы)')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('restaurant', models.ManyToManyField(related_name='dish', to='restaurant.restaurants', verbose_name='Ресторан')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
    ]
