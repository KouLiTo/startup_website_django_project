# Generated by Django 4.1.4 on 2022-12-31 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deploy_to_the_store', models.BooleanField(default=False)),
                ('design', models.BooleanField(default=False)),
                ('animation', models.BooleanField(default=False)),
                ('source_code', models.BooleanField(default=False)),
                ('marketing_consulting', models.BooleanField(default=False)),
                ('number_of_levels', models.PositiveSmallIntegerField()),
                ('awaiting_time', models.PositiveSmallIntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('surname', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(blank=True, default='', max_length=15, null=True, validators=[django.core.validators.RegexValidator('^[\\+]\\d{5,15}$')])),
                ('subject', models.CharField(choices=[('games', 'Games'), ('consulting', 'Consulting'), ('marketing', 'Marketing of games'), ('licence and deploying', 'Licence and Deploying'), ('other question', 'Other question')], max_length=40)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deploy_to_the_store', models.BooleanField(default=False)),
                ('design', models.BooleanField(default=False)),
                ('animation', models.BooleanField(default=False)),
                ('source_code', models.BooleanField(default=False)),
                ('marketing_consulting', models.BooleanField(default=False)),
                ('number_of_levels', models.PositiveSmallIntegerField()),
                ('awaiting_time', models.PositiveSmallIntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deploy_to_the_store', models.BooleanField(default=False)),
                ('design', models.BooleanField(default=False)),
                ('animation', models.BooleanField(default=False)),
                ('source_code', models.BooleanField(default=False)),
                ('marketing_consulting', models.BooleanField(default=False)),
                ('number_of_levels', models.PositiveSmallIntegerField()),
                ('awaiting_time', models.PositiveSmallIntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
