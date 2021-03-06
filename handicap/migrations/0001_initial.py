# Generated by Django 3.0.5 on 2020-04-19 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=20)),
                ('date_added', models.DateField(auto_now=True)),
                ('date_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('slope', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_added', models.DateField(auto_now=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handicap.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('differential', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('date_played', models.DateField(blank=True)),
                ('tee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handicap.Tee')),
            ],
        ),
    ]
