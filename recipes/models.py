from django.conf import settings
from django.db import models

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

    ingredients = models.JSONField(default=list)

    gallons = models.IntegerField(
        choices=GALLON_CHOICES,
        default=1
    )

def __str__(self):
    return f"{self.name} ({self.gallons} gal)"