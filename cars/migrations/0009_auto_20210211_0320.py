# Generated by Django 3.1.5 on 2021-02-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_auto_20210211_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drivetrain',
            field=models.CharField(choices=[('FWD', 'FWD'), ('RWD', 'RWD'), ('AWD', 'AWD')], max_length=10),
        ),
    ]
