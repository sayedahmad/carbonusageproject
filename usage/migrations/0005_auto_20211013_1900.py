# Generated by Django 3.2.8 on 2021-10-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0004_auto_20211013_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='usage_type',
            name='factor',
            field=models.FloatField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usage_type',
            name='unit',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
