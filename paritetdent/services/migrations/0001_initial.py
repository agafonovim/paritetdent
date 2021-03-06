# Generated by Django 3.0.4 on 2020-05-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stomatology', models.CharField(choices=[('ОБ', 'Общие виды работ '), ('Т', 'Стоматология терапевтическая'), ('Д', 'Детская стоматология'), ('ОР', 'Стоматология ортопедическая'), ('Х', 'Хирургическая стоматология')], max_length=2, verbose_name='Вид стоматологической помощи')),
                ('number', models.CharField(max_length=256, unique=True, verbose_name='Код услуги')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Наименование услуги')),
                ('price', models.PositiveIntegerField(help_text='Цена услуги в рублях', verbose_name='Цена')),
            ],
        ),
    ]
