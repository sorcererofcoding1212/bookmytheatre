from django.shortcuts import redirect
from django.http import HttpResponse
from ..movies.models import Movie
from django.contrib import messages

# Create your views here.


def handleNavbarRequest(request):
    movie_title = request.POST.get('movie_title')
    movie = Movie.objects.filter(title__icontains=movie_title).first()
    if not movie:
        messages.error(request, 'Invalid movie entered')
        return redirect('pages:home')
    return redirect('movies:movie', pk=movie.id)
