from django.conf import settings
from django.db import models

from datetime import date, timedelta

class Mead(models.Model):

    GALLON_CHOICES = [
        (1, "1 Gallon"),
        (3, "3 Gallons"),
        (5, "5 Gallons"),
    ]


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="meads"
    )

    name = models.CharField(default="Mead",max_length=50)

    equipment = models.JSONField(default=dict)

    ingredients = models.JSONField(default=dict)

    instructions = models.JSONField(default=dict)

    gallons = models.IntegerField(
        choices=GALLON_CHOICES,
        default=1
    )

    original_gravity = models.FloatField(default=0)
    final_gravity = models.FloatField(default=0)

    alcohol_by_volume = models.FloatField(default=0)

    fermentation_end_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.name} ({self.gallons} gal)"

    def calculate_abv(self):

        if self.original_gravity > 0 and self.final_gravity > 0:
            ABV = float((self.original_gravity - self.final_gravity) * 131.25)

            ABV = round(ABV,1)

            self.alcohol_by_volume = ABV

            self.save(update_fields=["alcohol_by_volume"])
        else:
            pass

    def add_fermentation_end_date(self):
        self.fermentation_end_date = date.today() + timedelta(weeks=4)

        self.save(update_fields=["fermentation_end_date"])