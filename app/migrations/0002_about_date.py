# Generated by Django 4.1.7 on 2023-04-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='date',
            field=models.DateField(default='2021-11-22'),
        ),
    ]
