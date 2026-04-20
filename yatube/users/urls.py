from django.contrib.auth.views import LoginView   # LoginView оставляем
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.logout_user, name='logout'),   # новая строка
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
]