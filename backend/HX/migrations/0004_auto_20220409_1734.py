# Generated by Django 3.2.5 on 2022-04-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HX', '0003_auto_20220408_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='hx',
            name='Tsetpt_live',
            field=models.FloatField(default=42.8),
        ),
        migrations.AlterField(
            model_name='hx',
            name='Tsetpt',
            field=models.FloatField(default=40.0),
        ),
    ]