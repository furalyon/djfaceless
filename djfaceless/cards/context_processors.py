from django.db.models import get_model

def choices(request):
    Card=get_model('cards','card')    
    b_temp = Card()
    return {
        'playerClasses': b_temp._meta.get_field('playerClass').choices,
        'card_cost_filter_options':{
            1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7+'
        }
    }
