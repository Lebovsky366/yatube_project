from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    # ---------- ДОБАВЛЕНО ----------
    path('create/', views.create_post, name='create_post'),
    path('api/posts/', views.api_posts, name='api_posts'),
    path('about/', views.about, name='about'),
]