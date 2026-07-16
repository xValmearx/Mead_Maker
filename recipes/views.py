from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Mead


class MeadListView(LoginRequiredMixin, ListView):
    model = Mead
    template_name = "mead/mead_list.html"
    context_object_name = "meads"

    def get_queryset(self):
        # Only return the logged-in user's meads
        return Mead.objects.filter(user=self.request.user)