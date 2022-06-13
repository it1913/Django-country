from django.shortcuts import render
from countries.models import Country,Town,Region,Attachment
from django.views.generic import ListView, DetailView


def index(request):
     num_countries = Country.objects.all().count()
     countries = Country.objects.order_by('-cName')[:3]
     context = {
          'num_countries': num_countries,
          'countries': countries
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
