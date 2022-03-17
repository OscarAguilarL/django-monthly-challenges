from django.urls import path

from . import views

# Urls de la subruta de 'challenges/'
urlpatterns = [
    path('<month>', views.monthly_challenge),
]
