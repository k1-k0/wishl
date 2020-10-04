# Generated by Django 3.1.1 on 2020-10-04 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishl_api', '0012_remove_moneybox_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='wish',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wishl_api.image'),
        ),
        migrations.AlterField(
            model_name='wish',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wishl_api.shop'),
        ),
    ]