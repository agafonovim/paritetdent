# Generated by Django 3.0.4 on 2020-05-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_auto_20200517_0753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classification',
            options={'verbose_name': 'Направление лечения', 'verbose_name_plural': 'Направления лечения'},
        ),
        migrations.AddField(
            model_name='classification',
            name='show',
            field=models.BooleanField(default=False, help_text='Максимум 4 элемента', verbose_name='Отображение на главной'),
        ),
    ]
