# Generated by Django 3.1.14 on 2022-05-04 14:38

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
