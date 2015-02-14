from django.core.management.base import BaseCommand, CommandError
import json
from djfaceless.cards.models import Card, Mechanic

def populate(filename='djfaceless/fixtures/AllSets.json'):
    with open (filename, "r") as myfile:
        data=myfile.read().replace('\n', '').replace('  ','')
    inventory = json.loads(data)
    for card_set, cards in dict.items(inventory):
        for card in cards:
            try:
                card['collectible']
                card['cost']
            except KeyError:
                pass
            else:
                mechanics = card.get('mechanics',[])
                if mechanics:
                    del(card['mechanics'])
                card_obj = Card.objects.create(
                    **card
                )
                for mechanic in mechanics:
                    mechanic_obj, _ = Mechanic.objects.get_or_create(name=mechanic)
                    card_obj.mechanics.add(mechanic_obj)

class Command(BaseCommand):
    args = ''
    help = 'Populate database with cards from the downloaded json'

    def handle(self, *args, **options):
        populate()
        self.stdout.write('Successfully filled cards')
