from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.template.defaultfilters import slugify

from .managers import CardManager

###################### ENTITIES ########################
# Whenever a new value for one of the entity fields(type, rarity, faction, race) is 
# entered create a record for it for quick filtering purposes

class AbstractEntity(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    slug = models.SlugField(_('Slug'), max_length=255,
        default=settings.FIELD_PLACEHOLDER, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(AbstractEntity, self).save(*args, **kwargs)

class Mechanic(AbstractEntity):
    pass

class Type(AbstractEntity):
    pass

class Rarity(AbstractEntity):
    class Meta:
        verbose_name_plural=_('rarities')

class PlayerClass(AbstractEntity):
    class Meta:
        verbose_name_plural=_('classes')

class Race(AbstractEntity):
    pass

class Faction(AbstractEntity):
    pass

class Set(AbstractEntity):
    pass

######################### CARD ########################

class Card(models.Model):
    game_id = models.CharField(_('game id'), max_length=255, unique=True)
    name = models.CharField(_('name'), max_length=255)
    type = models.CharField(_('type'), max_length=255)
    rarity = models.CharField(_('rarity'), max_length=255)
    playerClass = models.CharField(_('playerClass'), max_length=255,
        null=True, blank=True)
    NEUTRAL, TOKEN = 'Neutral', 'Token'

    cost = models.IntegerField(_('cost'), null=True, blank=True)
    attack = models.IntegerField(_('attack'), null=True, blank=True)
    health = models.IntegerField(_('health'), null=True, blank=True)
    durability = models.IntegerField(_('durability'), null=True, blank=True)

    mechanics = models.ManyToManyField(Mechanic, verbose_name= _('mechanics'),
        null=True)
    text = models.CharField(_('text'), max_length=255,
        null=True, blank=True)
    race = models.CharField(_('race'), max_length=255,
        null=True, blank=True)

    collectible = models.BooleanField(_('collectible'), default=False)

    faction = models.CharField(_('faction'), max_length=255,
        null=True, blank=True)
    inPlayText = models.CharField(_('inPlayText'), max_length=255,
        null=True, blank=True)
    flavor = models.CharField(_('flavor'), max_length=255,
        null=True, blank=True)
    artist = models.CharField(_('artist'), max_length=255,
        null=True, blank=True)
    elite = models.BooleanField(_('elite'), default=False)

    set = models.CharField(_('set'), max_length=255)
    howToGet = models.CharField(_('how to get'), max_length=255,
        null=True, blank=True)
    howToGetGold = models.CharField(_('how to get golden version'), max_length=255,
        null=True, blank=True)

    objects = CardManager()

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('game_id','name')

    def save(self, *args, **kwargs):
        super(Card, self).save(*args, **kwargs)
        Type.objects.get_or_create(name=self.type)
        Rarity.objects.get_or_create(name=self.rarity)
        PlayerClass.objects.get_or_create(name=self.playerClass)
        if self.race:
            Race.objects.get_or_create(name=self.race)
        if self.faction:
            Faction.objects.get_or_create(name=self.faction)
        Set.objects.get_or_create(name=self.set)
