from django.db import models

class CardManager(models.Manager):
    def collectible(self):
        return self.get_queryset().filter(
            collectible = True
        )

    def elite(self):
        return self.get_queryset().filter(
            elite = True
        )

