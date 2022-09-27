# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Models
from .models import *


class ProgramListView(ListView):
    """Program List View"""
    model = Program
    context_object_name = 'programs'
    template_name = 'wellness/programList.html'


class ProgramDetailView(DetailView):
    """Program Detail View"""
    model = Program
    context_object_name = 'program'
    template_name = 'wellness/programDetail.html'
