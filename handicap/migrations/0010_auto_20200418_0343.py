# Generated by Django 3.0.5 on 2020-04-18 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handicap', '0009_auto_20200418_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='date_played',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='score',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
