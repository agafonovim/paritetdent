# Generated by Django 3.0.4 on 2020-05-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20200510_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulation',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
    ]
