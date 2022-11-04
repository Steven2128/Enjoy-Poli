# Django
from django.urls import path
# Views
from .views import *

urlpatterns = [
    path('actividades-culturales/', ProgramByCulturalActivitiesListView.as_view(), name='cultural-activities-list'),
    path('actividades-culturales/<slug:title>', ProgramDetailView.as_view(), name='program-cultural-detail'),
    path('actividades-deportivas/', ProgramBySportActivitiesListView.as_view(), name='sport-activities-list'),
    path('actividades-deportivas/<slug:slug>', ProgramDetailView.as_view(), name='program-sport-detail'),
    path('consulta-medica-y-enfermeria/', ProgramByMedicalAndNursingActivitiesListView.as_view(), name='medical-activities-list'),
    path('consulta-medica-y-enfermeria/<slug:title>', ProgramDetailView.as_view(), name='program-medical-detail'),
    path('semillitas/', ProgramByPolyLittleSeedSActivitiesListView.as_view(), name='seed-activities-list'),
    path('semillitas/<slug:title>', ProgramDetailView.as_view(), name='program-seed-detail'),
    path('enroll-user/<str:title>', enroll_user, name='enroll-user'),
    path('bienestar/<slug:slug>', ProgramDetailView.as_view(), name='program-detail'),
    path('inscriptions/', ProgramListView.as_view(), name='inscriptions'),
]
