# Generated by Django 3.0.4 on 2020-05-10 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20200510_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='draft',
            new_name='published',
        ),
    ]
