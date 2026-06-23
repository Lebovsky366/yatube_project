from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # <-- добавить
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

def logout_user(request):
    logout(request)
    return render(request, 'users/logged_out.html')

# ---------- ДОБАВЛЕНО ----------
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})