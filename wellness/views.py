# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Models
from .models import *


class ProgramByCulturalActivitiesListView(ListView):
    """Program By Cultural Activities List View"""
    model = Program
    queryset = Program.objects.filter(activity='AC')
    context_object_name = 'programs'
    template_name = 'wellness/programList.html'


class ProgramBySportActivitiesListView(ListView):
    """Programs By Sport Activities List View"""
    model = Program
    queryset = Program.objects.filter(activity='AD')
    context_object_name = 'programs'
    template_name = 'wellness/programList.html'


class ProgramByMedicalAndNursingActivitiesListView(ListView):
    """Programs By Medical and Nursing Consultation List View"""
    model = Program
    queryset = Program.objects.filter(activity='CME')
    context_object_name = 'programs'
    template_name = 'wellness/programList.html'


class ProgramByPolyLittleSeedSActivitiesListView(ListView):
    """Programs By Poli Little Seed List View"""
    model = Program
    queryset = Program.objects.filter(activity='SP')
    context_object_name = 'programs'
    template_name = 'wellness/programList.html'


class ProgramDetailView(DetailView):
    """Programs Detail View"""
    model = Program
    template_name = 'wellness/programDetail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_object(self, **kwargs):
        return Program.objects.get(slug=self.kwargs['slug'])
