# Generated by Django 3.0.4 on 2020-05-15 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=18, verbose_name='Номер телефона')),
                ('about', models.TextField(max_length='2048', verbose_name='О себе')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.DeleteModel(
            name='Applications',
        ),
    ]