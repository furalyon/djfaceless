from django.shortcuts import render
from djfaceless.cards.models import Card

from django.core.paginator import Paginator

def filter_cards(playerClass='', cost=-1, search_text=''):
    if playerClass or cost>=0:
        query_dict = {}
        if playerClass:
            query_dict['playerClass__exact'] = playerClass
        if cost>=0:
            if cost==7:
                query_dict['cost__gte'] = cost
            else:
                query_dict['cost__exact'] = cost
        query_dict['collectible'] = True
        queryset = Card.objects.filter(**query_dict)
    else:
        queryset = Card.objects.collectible()

    if search_text:
        search_text_in_list = search_text.strip().lower().split(' ')
        print search_text_in_list
        result=[]
        for card in queryset:
            add_card = True
            for string in search_text_in_list:
                if string not in card.search_text.lower():
                    add_card = False
            if add_card:
                result.append(card)
    else:
        result = queryset

    return result


def browse(request):
    card_list = filter_cards(
        playerClass = request.GET.get('playerClass',''),
        cost = int(request.GET.get('cost',-1) or -1),
        search_text = request.GET.get('search_text',''),
    )
    return render(request, 'cards/browse.html', {
        'card_list' : card_list,
        })
