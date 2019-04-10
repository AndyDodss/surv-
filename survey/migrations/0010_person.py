# Generated by Django 2.1.7 on 2019-04-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_auto_20190404_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('incentive', models.BooleanField(default=False)),
            ],
        ),
    ]
