from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('profile/', views.profile, name='profile'),   # <-- добавить
]