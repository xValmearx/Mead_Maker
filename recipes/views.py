from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse


from .models import Mead
from mead_default import RECIPES, build_ingredient_dict, get_instructions, get_equipment


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
    
    def post(self, request, *args, **kwargs):

        mead = self.get_object()

        action = request.POST.get("action")


        if action == "update_original_gravity":

            amount = float(request.POST.get("amount"))

            if not amount:
                return JsonResponse({
                    "success": False,
                    "error": "No gravity provided"
                }, status=400)


            mead.original_gravity = amount
            mead.save()


            return JsonResponse({
                "success": True,
                "original_gravity": mead.original_gravity
            })


        elif action == "add_fermentation_end_date":
            mead.add_fermentation_end_date()

            return JsonResponse({
                "success": True,
                "date": mead.fermentation_end_date.strftime("%m/%d/%Y")
            })

        elif action == "calc_abv":
            mead.calculate_abv()

            return JsonResponse({
                "success": True,
                "alcohol_by_volume": mead.alcohol_by_volume
            })


        elif action == "update_final_gravity":

            amount = float(request.POST.get("amount"))

            if not amount:
                return JsonResponse({
                    "success": False,
                    "error": "No gravity provided"
                }, status=400)


            mead.final_gravity = amount
            mead.save()


            return JsonResponse({
                "success": True,
                "final_gravity": mead.final_gravity
            })


        return JsonResponse({
            "success": False,
            "error": "Invalid action"
        }, status=400)

    
    

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


        mead.ingredients = build_ingredient_dict(recipe,mead.gallons)

        mead.instructions = get_instructions(mead_type)

        mead.equipment = get_equipment(mead_type,mead.gallons)
        mead.save()

        return super().form_valid(form)

class MeadDeleteView(LoginRequiredMixin,DeleteView):

    model = Mead
    success_url = reverse_lazy("mead_list")

    def get_queryset(self):
        return Mead.objects.filter(user=self.request.user)

    