from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Peliculas, Series
from .forms import FormPelicula, FormSeries
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


class Peliculas01(ListView):
    model = Peliculas
    template_name = 'peliculas.html'
    
    

class Series01(ListView):
    model = Series
    template_name = 'series.html'
    


def prueba(request):
    peliculas = Peliculas.objects.all()
    series = Series.objects.all()
    items = list(peliculas)+list(series)
    for item in items: 
        item.is_pelicula = isinstance(item, Peliculas)
    paginator = Paginator(items,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'prueba.html', context)


def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Peliculas, pk=pk) 
    return render(request, 'articulo_pelicula.html', {'pelicula':pelicula})


def detalle_serie(request, pk):
    serie = get_object_or_404(Series, pk=pk) 
    return render(request, 'articulo_serie.html', {'serie':serie})

    
        
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



def about_me(request):
    return render(request, 'about_me.html')




    
    
    
    