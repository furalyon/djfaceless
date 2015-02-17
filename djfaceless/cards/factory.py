from . import models

class CardFactory(object):
    """
    To create/get cards from a dict of strings.

    Used when the input parameters do not realise about the 
    entity fields and simply passes strings.
    eg: when populating the card db using the downloaded API json file

    usage: 
     init with the list string parameters that the card has
     create card with create() -> This will get or create entities from string input
        before creating the card

    """
    def __init__(self, **kwargs):
        self.card_dict = kwargs

    def create(self):
        self.get_or_create_entities()
        manipulated_fields = (
            'id','type','rarity','playerClass','set','race','faction','mechanics'
        )
        unmanipulated_fields_dict = {
            key:value for key,value in self.card_dict.items() \
            if key not in manipulated_fields
        }

        card_obj = models.Card.objects.create(
            game_id = self.card_dict['id'],
            type = self.type,
            rarity = self.rarity,
            playerClass = self.playerClass,
            set = self.set,
            race = self.race,
            faction = self.faction,
            **unmanipulated_fields_dict
        )

        try:
            if self.mechanics:
                card_obj.mechanics.add(*self.mechanics)
        except:
            print self.mechanics
            raise


    def get_or_create_entities(self):
        self.type, _ = models.Type.objects.get_or_create(
            name = self.card_dict['type']
        )
        self.rarity, _ = models.Rarity.objects.get_or_create(
            name = self.card_dict.get('rarity', models.Rarity.TOKEN)
        )
        self.playerClass, _ = models.PlayerClass.objects.get_or_create(
            name = self.card_dict.get('playerClass', models.PlayerClass.NEUTRAL)
        )
        self.set, _ = models.Set.objects.get_or_create(
            name = self.card_dict['set']
        )

        race_string = self.card_dict.get('race','')
        self.race = None
        if race_string:
            self.race, _ = models.Race.objects.get_or_create(
                name = race_string
            )

        faction_string = self.card_dict.get('faction','')
        self.faction = None
        if faction_string:
            self.faction, _ = models.Faction.objects.get_or_create(
                name = faction_string
            )

        self.mechanics = []
        for mechanic in self.card_dict.get('mechanics',[]):
            mechanic_obj, _ = models.Mechanic.objects.get_or_create(
                name=mechanic
            )
            self.mechanics.append(mechanic_obj)
