from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout          # добавьте эту строку
from django.shortcuts import render             # добавьте эту строку
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

# Добавьте эту функцию
def logout_user(request):
    logout(request)
    return render(request, 'users/logged_out.html')