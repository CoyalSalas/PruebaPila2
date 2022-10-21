from django.urls import path, include 
from .views import SignUpView, HomeTemplateView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name= 'signup'  ),
    path('', HomeTemplateView.as_view(), name = 'home'),
    
]
