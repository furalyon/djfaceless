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

    def cards(self):
        return Card.objects.filter(type=self.name)

class Rarity(AbstractEntity):
    TOKEN = 'Token'
    class Meta:
        verbose_name_plural=_('rarities')

    def cards(self):
        return Card.objects.filter(rarity=self.name)

class Race(AbstractEntity):

    def cards(self):
        return Card.objects.filter(race=self.name)

class Faction(AbstractEntity):

    def cards(self):
        return Card.objects.filter(faction=self.name)

class Set(AbstractEntity):

    def cards(self):
        return Card.objects.filter(set=self.name)

######################### CARD ########################

class Card(models.Model):
    game_id = models.CharField(_('game id'), max_length=255, unique=True)
    name = models.CharField(_('name'), max_length=255)
    type = models.ForeignKey(Type, verbose_name=_('type'))
    rarity = models.ForeignKey(Rarity, verbose_name=_('rarity'))

    DRUID, HUNTER, MAGE, PALADIN, PRIEST, ROGUE, SHAMAN, WARLOCK, WARRIOR = (
        'Druid','Hunter','Mage','Paladin',
        'Priest','Rogue','Shaman','Warlock','Warrior'
    )
    PLAYER_CLASS_CHOICES = (
        (DRUID, _(DRUID)),
        (HUNTER,_(HUNTER)),
        (MAGE,_(MAGE)),
        (PALADIN,_(PALADIN)),
        (PRIEST,_(PRIEST)),
        (ROGUE,_(ROGUE)),
        (SHAMAN,_(SHAMAN)),
        (WARLOCK,_(WARLOCK)),
        (WARRIOR,_(WARRIOR)),
    )
    playerClass = models.CharField(_('Class'), max_length=255,
        choices=PLAYER_CLASS_CHOICES, null=True, blank=True)

    cost = models.IntegerField(_('cost'), null=True, blank=True)
    attack = models.IntegerField(_('attack'), null=True, blank=True)
    health = models.IntegerField(_('health'), null=True, blank=True)
    durability = models.IntegerField(_('durability'), null=True, blank=True)

    mechanics = models.ManyToManyField(Mechanic, verbose_name= _('mechanics'),
        null=True)
    text = models.CharField(_('text'), max_length=255,
        null=True, blank=True)
    race = models.ForeignKey(Race, verbose_name=_('race'),
        null=True, blank=True)

    collectible = models.BooleanField(_('collectible'), default=False)

    faction = models.ForeignKey(Faction, verbose_name=_('faction'),
        null=True, blank=True)
    inPlayText = models.CharField(_('in Play Text'), max_length=255,
        null=True, blank=True)
    flavor = models.CharField(_('flavor'), max_length=255,
        null=True, blank=True)
    artist = models.CharField(_('artist'), max_length=255,
        null=True, blank=True)
    elite = models.BooleanField(_('elite'), default=False)

    set = models.ForeignKey(Set, verbose_name=_('set'))
    howToGet = models.CharField(_('how to get'), max_length=255,
        null=True, blank=True)
    howToGetGold = models.CharField(_('how to get golden version'), max_length=255,
        null=True, blank=True)

    objects = CardManager()

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('game_id','name')
        ordering = ('playerClass','name')
