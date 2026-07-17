from django.urls import path
from .views import MeadListView 

# urls.py

from django.urls import path
from .views import MeadCreateView

urlpatterns = [
    path("", MeadListView.as_view(), name="mead_list"),

    path(
        "create/<slug:mead_type>/",
        MeadCreateView.as_view(),
        name="mead_create",
    ),
]