# Django
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
# Models
from .models import *
# Models User
from users.models import *

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

    def get_context_data(self, *args, **kwargs):
        context = super(ProgramDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context['program'] = instance
        context['schedule'] = Schedule.objects.filter(program=instance).first()
        is_enroll = Program.objects.filter(students__user=self.request.user, slug=instance.slug).first()
        if is_enroll:
            context['is_enroll'] = True
        else:
            context['is_enroll'] = False
        return context

    def get_object(self, **kwargs):
        return Program.objects.get(slug=self.kwargs['slug'])


def enroll_user(request, title):
    """Inscribir a un estudiante a un programa"""
    if not Program.objects.filter(students__user=request.user, slug=title).first():
        program = Program.objects.get(slug=title)
        program.students.add(request.user.student)
        if program.current_capacity_available != 0:
            program.current_capacity_available -= 1
            program.save()
            messages.success(request, '¡Inscrito exitosamente!')
        else:
            messages.error(request, '¡Se ha alcanzado el maximo de cupo para este programa!')
    if program.activity == 'AC':
        return redirect('program-cultural-detail', program.slug)
    elif program.activity == 'AD':
        return redirect('program-sport-detail', program.slug)
    elif program.activity == 'CME':
        return redirect('program-medical-detail', program.slug)
    elif program.activity == 'SP':
        return redirect('program-seed-detail', program.slug)


class ProgramListView(ListView):
    """Programs List View"""
    model = Program
    context_object_name = 'programs'
    template_name = 'wellness/myInscriptions.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProgramListView, self).get_context_data(*args, **kwargs)
        context['programs'] = Program.objects.filter(students__user=self.request.user)
        return context
