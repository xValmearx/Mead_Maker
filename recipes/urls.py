from django.urls import path
from .views import MeadListView 

# urls.py

from django.urls import path
from .views import MeadCreateView, MeadDetailView

urlpatterns = [
    path("", MeadListView.as_view(), name="mead_list"),

    path("<int:pk>/", 
         MeadDetailView.as_view(), 
         name="mead_detail"
    ),

    path(
        "create/<slug:mead_type>/",
        MeadCreateView.as_view(),
        name="mead_create",
    ),
]