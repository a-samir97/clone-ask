# Generated by Django 3.0.6 on 2020-05-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200508_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
