# Generated by Django 4.2.1 on 2023-05-12 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apart',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='apart',
            name='quantityRoom',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
