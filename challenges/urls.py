from django.urls import path

from . import views

# Urls de la subruta de 'challenges/'
urlpatterns = [
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='month-challenge'),
]
