from django.shortcuts import render
from django.views.generic import ListView
from djfaceless.cards.models import Card

#install django-filters for filtering

#use Paginator class. It has all the stuff I need
from django.core.paginator import Paginator

class BrowseView(ListView):
    queryset = Card.objects.collectible()
    template_name = 'cards/browse.html'
    paginate_by = 20
