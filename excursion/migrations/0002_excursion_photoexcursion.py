# Generated by Django 3.1.6 on 2021-02-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='photoexcursion',
            field=models.ImageField(default=False, upload_to='pics'),
        ),
    ]
