# Generated by Django 3.2.19 on 2023-06-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
