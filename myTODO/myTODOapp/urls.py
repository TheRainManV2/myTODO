# Here we define the paths to the different views in views.py

from django.urls import path
from . import views

urlpatterns = [
        path("<int:id>", views.index, name="index"),
]
