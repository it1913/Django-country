from django.shortcuts import render
from countries.models import Country,Town,Region,Attachment
from django.views.generic import ListView, DetailView


def index(request):
     context = {
          'countryByDensity': Country.objects.order_by('-cPopulationDensity')[:5],
          'regionByPopulation': Region.objects.order_by('-rPopulation')[:10],
          'country': Country.objects.order_by('-cAbbr')[:5],
     }
     return render(request, 'index.html', context=context)


class CountryListView(ListView):
     model = Country
     context_object_name = 'country_list'
     template_name = 'country/list.html'


class CountryDetailView(DetailView):
     model = Country
     context_object_name = 'country_detail'
     template_name = 'country/detail.html'
