# Generated by Django 2.0.6 on 2018-10-22 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0003_auto_20181022_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currentBal',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='emergency',
            field=models.CharField(max_length=10),
        ),
    ]
