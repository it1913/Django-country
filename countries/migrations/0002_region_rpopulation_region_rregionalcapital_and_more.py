# Generated by Django 4.0.4 on 2022-04-13 17:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='rPopulation',
            field=models.IntegerField(blank=True, default=1, verbose_name='Populace kraje nebo spolkového/unijního státu'),
        ),
        migrations.AddField(
            model_name='region',
            name='rRegionalCapital',
            field=models.CharField(default='.', max_length=50, verbose_name='Hlavní město kraje nebo spolkového/unijního státu'),
        ),
        migrations.AlterField(
            model_name='country',
            name='cPopulation',
            field=models.IntegerField(blank=True, default=1, verbose_name='Populace země'),
        ),
        migrations.AlterField(
            model_name='country',
            name='cSummary',
            field=models.CharField(max_length=2000, verbose_name='Shrnutí země'),
        ),
        migrations.AlterField(
            model_name='region',
            name='rAbbr',
            field=models.CharField(blank=True, default='.', help_text='Zadejte zkratku kraje nebo spolkového/unijního státu např. STČ, PHA', max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Zkratka kraje nebo spolkového/unijního státu'),
        ),
        migrations.AlterField(
            model_name='region',
            name='rCountry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.country', verbose_name='Země'),
        ),
        migrations.AlterField(
            model_name='region',
            name='rName',
            field=models.CharField(default='.', help_text='Zadejte jméno kraje nebo spolkového/unijního státu', max_length=50, unique=True, verbose_name='Jméno regionu nebo spolkového/unijního státu'),
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tName', models.CharField(default='.', help_text='Zadejte jméno města', max_length=50, unique=True, verbose_name='Jméno města')),
                ('tPopulation', models.IntegerField(blank=True, default=1, verbose_name='Populace města')),
                ('tRegion', models.ForeignKey(default='.', on_delete=django.db.models.deletion.CASCADE, to='countries.region', verbose_name='Region')),
            ],
            options={
                'ordering': ['tName'],
            },
        ),
    ]
