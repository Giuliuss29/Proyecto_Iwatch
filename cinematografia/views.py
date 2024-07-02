from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Peliculas, Series
from .forms import FormPelicula, FormSeries
from django.contrib.auth.decorators import login_required


class Peliculas(ListView):
    model = Peliculas
    template_name = 'peliculas.html'
    
    

class Series(ListView):
    model = Series
    template_name = 'series.html'
    


def inicio(request):
    return render(request, 'inicio.html')



class Prueba(ListView):
    model = Peliculas
    template_name = 'prueba.html'
    
        
@login_required(login_url='login')    
def agregar_peli(request):
    
    if request.method == 'POST':
        formulario = FormPelicula(request.POST,request.FILES)
        if formulario.is_valid():
            pelicula=formulario.save(commit=False)
            pelicula.usuario = request.user
            pelicula.save()
            return redirect('inicio')
    else: 
        formulario=FormPelicula()
    return render(request,'agregar_peli.html',{'formulario':formulario})



@login_required(login_url='login')    
def agregar_series(request):
    
    if request.method == 'POST':
        formulario = FormSeries(request.POST,request.FILES)
        if formulario.is_valid():
            pelicula=formulario.save(commit=False)
            pelicula.usuario = request.user
            pelicula.save()
            return redirect('inicio')
    else: 
        formulario=FormSeries()
    return render(request,'agregar_series.html',{'formulario':formulario})  




    
    
    
    