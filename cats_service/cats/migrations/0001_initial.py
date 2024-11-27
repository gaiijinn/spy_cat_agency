# Generated by Django 3.2.16 on 2024-11-27 10:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('breed', models.CharField(max_length=256)),
                ('years_of_experience', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]
