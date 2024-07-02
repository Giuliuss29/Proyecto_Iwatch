from django.urls import path
from cinematografia import views
from .views import agregar_peli, agregar_series, inicio

urlpatterns = [
    path('',inicio, name='inicio'),
    path('prueba/', views.Prueba.as_view(), name='prueba'),
    path('peliculas/', views.Peliculas.as_view(), name='peliculas'),
    path('series/', views.Series.as_view(), name='series'),
    path('agregar_peli/', agregar_peli,name='agregar_peli'),
    path('agregar_series/', agregar_series,name='agregar_series'),
    
    
    
]
