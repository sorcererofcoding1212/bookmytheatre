from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Movie

# Create your views here.

class MovieDetailView(DetailView):
    template_name = 'movies/movie.html'
    context_object_name = 'movie'
    model = Movie
