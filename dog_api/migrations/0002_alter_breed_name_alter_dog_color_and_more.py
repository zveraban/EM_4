# Generated by Django 5.1.5 on 2025-01-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dog',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dog',
            name='favorite_food',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dog',
            name='favorite_toy',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
