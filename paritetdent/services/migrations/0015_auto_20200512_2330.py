# Generated by Django 3.0.4 on 2020-05-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20200512_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
    ]