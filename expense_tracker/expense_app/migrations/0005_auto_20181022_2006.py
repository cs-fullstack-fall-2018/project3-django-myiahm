# Generated by Django 2.0.6 on 2018-10-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0004_auto_20181022_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currentBal',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='emergency',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
