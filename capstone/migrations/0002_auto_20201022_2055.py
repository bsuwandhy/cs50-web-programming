# Generated by Django 3.1 on 2020-10-22 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='name',
            new_name='model',
        ),
    ]
