import json

from django.core.management.base import BaseCommand, CommandError

from djfaceless.cards.models import Card, Mechanic

def populate(filename='djfaceless/fixtures/AllSets.json'):
    with open (filename, "r") as myfile:
        data=myfile.read().replace('\n', '').replace('  ','')
    inventory = json.loads(data)
    for card_set, cards in dict.items(inventory):
        if card_set != 'Debug':
            for card in cards:
                card_type = card.get('type','')
                if card_type in ('Minion', 'Spell', 'Weapon'):
                    try:
                        card['playerClass'] = card.get('playerClass', Card.NEUTRAL)
                        card['rarity'] = card.get('rarity', Card.TOKEN)
                        card['game_id'] = card['id']
                        del(card['id'])

                        mechanics = card.get('mechanics',[])
                        try:
                            del(card['mechanics'])
                        except KeyError:
                            pass

                        card_obj = Card.objects.create(
                            set = card_set,
                            **card
                        )

                        for mechanic in mechanics:
                            mechanic_obj, _ = Mechanic.objects.get_or_create(
                                name=mechanic
                            )
                            card_obj.mechanics.add(mechanic_obj)
                    except Exception,e:
                        print card
                        # print '\n%s'%e
                        raise

class Command(BaseCommand):
    args = ''
    help = 'Populate database with cards from the downloaded json'

    def handle(self, *args, **options):
        populate()
        self.stdout.write('Successfully filled cards')