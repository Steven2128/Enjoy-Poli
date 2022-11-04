# Django
from django.urls import path
# Views
from .views import *

urlpatterns = [
    # SignUp
    path('signup/', SignupView.as_view(), name='signup'),
]
