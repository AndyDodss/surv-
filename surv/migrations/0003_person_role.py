# Generated by Django 2.1.7 on 2019-04-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surv', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.IntegerField(default=-1, max_length=1),
        ),
    ]