# Generated by Django 4.1.3 on 2023-02-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_name',
            field=models.CharField(max_length=20),
        ),
    ]
