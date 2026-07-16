from django.contrib import admin
from .models import Mead


@admin.register(Mead)
class MeadAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "gallons")
    list_filter = ("gallons",)
    search_fields = ("name", "user__username")

