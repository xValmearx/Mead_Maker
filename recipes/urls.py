from django.urls import path
from .views import MeadListView #, MeadDetailView

urlpatterns = [
    path("", MeadListView.as_view(), name="mead_list"),
    #path("<int:pk>/", MeadDetailView.as_view(), name="mead_detail"),
]