# Generated by Django 2.1.7 on 2019-04-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surv', '0011_auto_20190420_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
    ]