import imp
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class HomeTemplateView(TemplateView):
    template_name = 'home.html'