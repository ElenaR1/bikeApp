# Generated by Django 2.2.1 on 2019-06-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='model',
            field=models.CharField(max_length=256),
        ),
    ]
