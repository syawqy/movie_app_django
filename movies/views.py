from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from typing import Any, Dict
from .models import Movie, MpaaRating


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    min_search_length = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search', '').strip()
        
        if len(search_term) >= self.min_search_length:
            return queryset.filter(name__icontains=search_term)
        return queryset


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'


def movie_search(request: HttpRequest) -> JsonResponse:
    search_term = request.GET.get('q', '').strip()
    movies = get_movie_search_results(search_term)
    return JsonResponse({'results': serialize_movies(movies)}, safe=False)


def get_movie_search_results(search_term: str, max_results: int = 10):
    if not search_term:
        return Movie.objects.none()
        
    return Movie.objects.filter(name__icontains=search_term)[:max_results]


def serialize_movies(movies) -> list[Dict[str, Any]]:
    return [
        {
            'id': movie.id,
            'name': movie.name,
            'img_path': movie.img_path,
            'rating': movie.user_rating,
            'duration': movie.duration
        } for movie in movies
    ]