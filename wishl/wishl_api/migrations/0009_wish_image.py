# Generated by Django 3.1.1 on 2020-09-29 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishl_api', '0008_auto_20200929_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='image',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wishl_api.image'),
            preserve_default=False,
        ),
    ]