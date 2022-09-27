# Django
from django.urls import path
# Views
from .views import *

urlpatterns = [
    path('', ProgramListView.as_view(), name='program-list'),
    path('<int:pk>/', ProgramDetailView.as_view(), name='program-detail'),
]
