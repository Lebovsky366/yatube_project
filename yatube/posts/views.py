from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model   # <-- ДОБАВЛЕНО
from .models import Post, Group

User = get_user_model()   # <-- ДОБАВЛЕНО

def index(request):
    search_query = request.GET.get('q', '')
    posts = Post.objects.select_related('author', 'group').order_by('-pub_date')
    if search_query:
        posts = posts.filter(text__icontains=search_query)
    posts = posts[:10]

    # ---------- ДОБАВЛЕНО ДЛЯ СТАТИСТИКИ ----------
    groups = Group.objects.all()
    user_count = User.objects.count()

    context = {
        'posts': posts,
        'search_query': search_query,
        'groups': groups,           # <-- ДОБАВЛЕНО
        'user_count': user_count,   # <-- ДОБАВЛЕНО
        'group_count': groups.count(),  # <-- ДОБАВЛЕНО
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author').order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

# ---------- ДОБАВЛЕНО ДЛЯ ТЕМЫ 1 (декоратор) ----------
@login_required
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        group_id = request.POST.get('group')
        if text:
            group = None
            if group_id:
                group = Group.objects.get(id=group_id)
            Post.objects.create(
                author=request.user,
                text=text,
                group=group
            )
            return redirect('posts:index')
    groups = Group.objects.all()
    return render(request, 'posts/create_post.html', {'groups': groups})

# ---------- ДОБАВЛЕНО ДЛЯ ТЕМЫ 2 (сериализатор) ----------
def api_posts(request):
    posts = Post.objects.select_related('author', 'group').all()
    data = [post.to_dict() for post in posts]
    return JsonResponse(data, safe=False)

def about(request):
    return render(request, 'posts/about.html')