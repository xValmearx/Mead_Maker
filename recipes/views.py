from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .models import Mead
from mead_default import RECIPES


class MeadListView(LoginRequiredMixin, ListView):
    model = Mead
    template_name = "mead/mead_list.html"
    context_object_name = "meads"

    def get_queryset(self):
        # Only return the logged-in user's meads
        return Mead.objects.filter(user=self.request.user)
    

class MeadDetailView(LoginRequiredMixin, DetailView):
    model = Mead
    template_name = "mead/detail.html"
    context_object_name = "mead"

    def get_queryset(self):
        # Only allow users to view their own meads
        return Mead.objects.filter(user=self.request.user)
    

class MeadCreateView(LoginRequiredMixin,CreateView):
    model = Mead
    fields = ["gallons"]
    template_name = "mead/create.html"
    success_url = reverse_lazy("mead_list")

    def get_queryset(self):
        return Mead.objects.filter(user=self.request.user)

    def form_valid(self, form):
        mead = form.save(commit=False)

        # Assign the logged-in user
        mead.user = self.request.user

        # Get the recipe from the slug
        mead_type = self.kwargs["mead_type"]
        recipe = RECIPES[mead_type]

        # Give the mead a default name
        mead.name = mead_type.replace("-", " ").title()

        # Build the ingredients JSON
        ingredients = {}

        for ingredient, data in recipe.items():
            ingredients[ingredient] = {
                "amount": data["amount"][mead.gallons],
                "unit": data["unit"],
            }

        mead.ingredients = ingredients

        mead.save()

        return super().form_valid(form)