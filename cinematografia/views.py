from django.shortcuts import render
from django.views.generic import ListView
from cinematografia.models import Peliculas


class Peliculas(ListView):
    model = Peliculas
    template_name = 'cinematografia/peliculas.html'
    context_object_name = 'peliculas'