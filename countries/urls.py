from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.CountryListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.CountryDetailView.as_view(), name='country_detail'),
]


