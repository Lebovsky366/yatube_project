from django.shortcuts import render, get_object_or_404
from .models import Post, Group   # импортируем модели

def index(request):
    # Получаем 10 последних постов (сортировка по дате, новые сверху)
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    # Получаем группу по slug, если не найдено – ошибка 404
    group = get_object_or_404(Group, slug=slug)
    # Получаем посты, принадлежащие этой группе
    posts = group.posts.order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)