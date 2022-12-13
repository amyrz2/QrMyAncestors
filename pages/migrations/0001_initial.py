# Generated by Django 4.1.2 on 2022-12-13 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Deceased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1)),
                ('birthdate', models.DateField()),
                ('birth_city', models.CharField(max_length=30)),
                ('birth_state', models.CharField(max_length=30)),
                ('birth_country', models.CharField(max_length=30)),
                ('deathdate', models.DateField()),
                ('death_city', models.CharField(max_length=30)),
                ('death_state', models.CharField(max_length=30)),
                ('death_country', models.CharField(max_length=30)),
                ('bio', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.user')),
            ],
            options={
                'db_table': 'deceased',
            },
        ),
    ]
