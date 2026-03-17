from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница проекта Yatube')

def group_posts(request, slug):
    return HttpResponse(f'Здесь будет информация о группе: {slug}')