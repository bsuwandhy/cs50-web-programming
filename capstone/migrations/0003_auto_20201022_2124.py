# Generated by Django 3.1 on 2020-10-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0002_auto_20201022_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoesize',
            name='size',
            field=models.DecimalField(choices=[('5.0', '5'), ('5.5', '5.5'), ('6.0', '6'), ('6.5', '6.5'), ('7.0', '7'), ('7.5', '7.5'), ('8.0', '8'), ('8.5', '8.5'), ('9.0', '9'), ('9.5', '9.5'), ('10.0', '10'), ('10.5', '10.5'), ('11.0', '11'), ('11.5', '11.5'), ('12.0', '12'), ('12.5', '12.5'), ('13.0', '13'), ('13.5', '13.5'), ('14.0', '14'), ('14.5', '14.5')], decimal_places=1, max_digits=3),
        ),
    ]
