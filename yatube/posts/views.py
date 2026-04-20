from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    # Получаем поисковый запрос из GET-параметра 'q' (по умолчанию пустая строка)
    search_query = request.GET.get('q', '')
    
    # Базовый запрос: выбираем посты с подгрузкой связанных объектов author и group
    # Это избавляет от дополнительных запросов при обращении к post.author и post.group в шаблоне
    posts = Post.objects.select_related('author', 'group').order_by('-pub_date')
    
    # Если введён поисковый запрос, фильтруем посты по тексту (регистронезависимо)
    if search_query:
        posts = posts.filter(text__icontains=search_query)
    
    # Ограничиваем выборку 10 последними постами (после фильтрации)
    posts = posts[:10]
    
    context = {
        'posts': posts,
        'search_query': search_query,   # передаём запрос в шаблон, чтобы сохранить его в поле ввода
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    # Для страницы группы тоже оптимизируем запрос, подгружая автора
    posts = group.posts.select_related('author').order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)