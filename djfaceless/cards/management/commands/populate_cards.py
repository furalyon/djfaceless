import json

from django.core.management.base import BaseCommand, CommandError

from djfaceless.cards.models import Card, Mechanic
from djfaceless.cards.factory import CardFactory

def file_as_string(filename):
    with open (filename, "r") as myfile:
        return myfile.read().replace('\n', '')

def populate(filename='djfaceless/fixtures/AllSets.json'):
    data = file_as_string(filename)
    inventory = json.loads(data)
    for card_set, cards in dict.items(inventory):
        if card_set != 'Debug':
            for card in cards:
                card_type = card.get('type','')
                if card_type in ('Minion', 'Spell', 'Weapon'):
                    try:
                        card_factory = CardFactory(set=card_set,**card)
                        card_factory.create()
                    except:
                        print card
                        raise

class Command(BaseCommand):
    args = ''
    help = 'Populate database with cards from the downloaded json'

    def handle(self, *args, **options):
        populate()
        self.stdout.write('Successfully filled cards')
