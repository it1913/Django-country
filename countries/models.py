from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


def attachment_path(instance, filename):
    return "countries/" + str(instance) + "/attachments/" + filename


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
    img = models.ImageField(upload_to=attachment_path, blank=True, null=True, verbose_name="Vlajka státu")
    cPopulationDensity = models.IntegerField(verbose_name='Hustota zalidnění', blank=True, default=1);
    cArea = models.IntegerField(verbose_name='Rozloha státu', blank=True, default=1);

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


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")
    TYPE_OF_ATTACHMENT = (('audio', 'Audio'),
                          ('image', 'Image'),
                          ('text', 'Text'),
                          ('video', 'Video'),
                          ('other', 'Other'),)

    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True, default='image',
                            help_text='Select allowed attachment type', verbose_name="Attachment type")
    img = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-last_update", "type"]

    def __str__(self):
        return f"{self.title}, ({self.type})"
