from django.db import models
from django.core.validators import MinLengthValidator


class Aliance:
    pass


class Country(models.Model):

    SYSTEMS = [
        ('Prezidentská republika', 'Prezidentská republika'),
        ('Poloprezidentská republika', 'Poloprezidentská republika'),
        ('Parlamentní republika', 'Parlamentní republika'),
        ('Konstituční monarchie', 'Konstituční monarchie'),
        ('Absolutní monarchie', 'Absolutní monarchie')
    ]

    cAbbr = models.CharField(max_length=3, unique=True, validators=[MinLengthValidator(3)], verbose_name='Zkratka země', help_text='Zadejte zkratku země např. CZE, FRA')
    cName = models.CharField(max_length=50, unique=True, verbose_name='Jméno země', help_text='Zadejte jméno země např. Česká republika')
    cSystem = models.CharField(max_length=50, choices=SYSTEMS, verbose_name='Státní zřízení')
    cPopulation = models.IntegerField(verbose_name='Populace země', blank=True, default=1)
    cSummary = models.TextField(verbose_name='Shrnutí země')
    cCapital = models.CharField(max_length=50, unique=True, verbose_name='Hlavní město')
    # cFlag =

    class Meta:
        ordering = ['cName']

    def __str__(self):
        return self.cName


class Tourism:
    pass


class Region(models.Model):
    rCountry = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Země')
    rAbbr = models.CharField(max_length=3, blank=True, unique=True, validators=[MinLengthValidator(2)], verbose_name='Zkratka kraje nebo spolkového/unijního státu', help_text='Zadejte zkratku kraje nebo spolkového/unijního státu např. STČ, PHA', default=".")
    rName = models.CharField(max_length=50, unique=True, verbose_name='Jméno regionu nebo spolkového/unijního státu', help_text='Zadejte jméno kraje nebo spolkového/unijního státu', default=".")
    rPopulation = models.IntegerField(verbose_name='Populace kraje nebo spolkového/unijního státu', blank=True, default=1)
    rRegionalCapital = models.CharField(max_length=50, verbose_name='Hlavní město kraje nebo spolkového/unijního státu', default=".")
    # rFlag - Potřeboval bych doučit, jak ukládání obrázků
    # rSymbol

    class Meta:
        ordering = ['rCountry__cName']

    def __str__(self):
        return self.rName


class Town(models.Model):
    tRegion = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region', default=".")
    tName = models.CharField(max_length=50, unique=True, verbose_name='Jméno města', help_text='Zadejte jméno města', default=".")
    tPopulation = models.IntegerField(verbose_name='Populace města', blank=True, default=1)
    class Meta:
        ordering = ['tName']

    def __str__(self):
        return self.tName
