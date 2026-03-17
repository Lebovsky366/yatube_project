from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница с постами по группам (slug)
    path('group/<slug:slug>/', views.group_posts),
]