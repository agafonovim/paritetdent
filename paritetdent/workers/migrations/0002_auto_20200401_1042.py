# Generated by Django 3.0.4 on 2020-04-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workers',
            options={'verbose_name': 'Сотрудника', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AddField(
            model_name='workers',
            name='sex',
            field=models.CharField(choices=[('М', 'Мужчина'), ('Ж', 'Женщина')], default=1, max_length=1, verbose_name='Пол'),
            preserve_default=False,
        ),
    ]
