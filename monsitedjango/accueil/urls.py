from django.urls import path
from .views import displayFilms

urlpatterns = [
    path('acc2/', displayFilms, name='pageAccueil'),
]
