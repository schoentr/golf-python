# Generated by Django 3.0.5 on 2020-04-23 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handicap', '0006_remove_course_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date_modified',
        ),
    ]