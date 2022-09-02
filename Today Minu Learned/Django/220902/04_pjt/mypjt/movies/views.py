from django.shortcuts import render, redirect
from .models import Movies

# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

def new(request):
    context = {
        'is_True':True
    }
    return render(request, 'movies/new.html', context)

def create(request):
    context = dict()
    title = request.POST.get('title')
    if len(title) <= 0:
        context['title_is_True'] = False
    else:
        context['title'] = title
    audience = request.POST.get('audience')
    if len(audience) <= 0:
        context['audience_is_True'] = False
    else:
        context['audience'] = audience
    release_date = request.POST.get('release_date')
    if len(release_date) <= 0:
        context['release_date_is_True'] = False
    else:
        context['release_date'] = release_date
    genre = request.POST.get('genre')
    if genre == '장르를 선택하세요.':
        context['genre_is_True'] = False
    else:
        context['genre'] = genre
    score = request.POST.get('score')
    if len(score) <= 0:
        context['score_is_True'] = False
    else:
        context['score'] = score
    poster_url = request.POST.get('poster_url')
    if len(poster_url) <= 0:
        context['poster_url_is_True'] = False
    else:
        context['poster_url'] = poster_url
    description = request.POST.get('description')
    if len(description) <= 0:
        context['description_is_True'] = False
    else:
        context['description'] = description
    if False in context.values():
        return render(request, 'movies/new.html', context)
    movies = Movies(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
    movies.save()
    return redirect('movies:detail', movies.pk)

def detail(request, pk):
    movies = Movies.objects.get(pk=pk)
    context = {
        'movies': movies
    }
    return render(request, 'movies/detail.html', context)

def edit(request, pk):
    movies = Movies.objects.get(pk=pk)
    context = {
        'movies': movies
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    movies = Movies.objects.get(pk=pk)
    movies.title = request.POST.get('title')
    movies.audience = request.POST.get('audience')
    movies.release_date = request.POST.get('release_date')
    movies.genre = request.POST.get('genre')
    movies.score = request.POST.get('score')
    movies.poster_url = request.POST.get('poster_url')
    movies.description = request.POST.get('description')
    movies.save()
    return redirect('movies:detail', movies.pk)

def delete(request, pk):
    movies = Movies.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')

def search(request):
    word = request.GET.get('search_title')
    movies = Movies.objects.filter(title__contains=word)
    if not word:
        context = {
            'movies' : False
        }
    else:
        context = {
            'movies': movies
        }
    return render(request, 'movies/search.html', context)

