from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Film
from django.http import Http404


def displayFilms(request):

    film = Film(title="Le Seigneur des Anneaux - La Communauté de l'Anneau", releaseYear=2001, director="Peter Jackson")    
    film.save()

    template = loader.get_template('accueil/pageAccueil.html')

    context = {
        "film": film
    }
    return HttpResponse(template.render(context, request))
