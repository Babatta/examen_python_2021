# Generated by Django 3.1.6 on 2021-02-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0003_auto_20210226_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyage',
            name='classe',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
