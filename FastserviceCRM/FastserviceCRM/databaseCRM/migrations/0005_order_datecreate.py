# Generated by Django 5.0.6 on 2024-06-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseCRM', '0004_alter_typeorder_descriptiontypeorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dateCreate',
            field=models.DateTimeField(null=True, verbose_name='Дата создания'),
        ),
    ]
