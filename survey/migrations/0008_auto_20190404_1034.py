# Generated by Django 2.1.7 on 2019-04-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20190404_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='BName',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='source',
            name='SName',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='waiters',
            name='W_Name',
            field=models.CharField(max_length=150),
        ),
    ]
