# Generated by Django 3.0.4 on 2020-05-10 00:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200506_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('base', models.CharField(choices=[('П', 'Постоянно '), ('Н', 'Непостоянно')], max_length=1, verbose_name='Время действия скидки')),
                ('expiration_date', models.DateField(help_text='Если скидка постоянная, то можно не указывать', null=True, verbose_name='Действует до')),
                ('draft', models.BooleanField(default=0, verbose_name='Черновик')),
            ],
            options={
                'verbose_name': 'Акции',
                'verbose_name_plural': 'Акция',
            },
        ),
    ]
