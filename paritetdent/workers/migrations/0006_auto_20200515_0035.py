# Generated by Django 3.0.4 on 2020-05-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_auto_20200515_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='experience',
            field=models.CharField(default=1, help_text='Пример: 10 лет', max_length=32, verbose_name='Стаж работы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workers',
            name='position',
            field=models.ManyToManyField(help_text="Зажмите 'Ctrl' или 'Command' на Mac, чтобы выбрать несколько должностей.", to='workers.Positions', verbose_name='Должность'),
        ),
    ]
