from django.urls import path
from cinematografia import views


urlpatterns = [
    path('peliculas/', views.Peliculas.as_view(), name='peliculas')
]
