# Generated by Django 3.1.1 on 2020-09-28 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishl_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='location',
            new_name='shop',
        ),
    ]
