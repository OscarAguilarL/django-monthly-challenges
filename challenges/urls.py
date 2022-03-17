from django.urls import path

from . import views

# Urls de la subruta de 'challenges/'
urlpatterns = [
    path("january", views.index)
]
