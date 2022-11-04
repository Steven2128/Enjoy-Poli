# Django
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Forms
from .forms import SignupForm


class SignupView(CreateView):
    """Signup View"""
    model = User
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('index')

