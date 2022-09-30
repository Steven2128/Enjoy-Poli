# Django
from django.contrib.auth.models import User
from django.db import models
# Models wellness
from wellness.models import *


class Teacher(models.Model):
    """Model Teacher"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, blank=False, null=False, verbose_name='Especialización del docente')

    def __str__(self):
        return "{} - {}".format(self.user.get_full_name(), self.specialization)

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'


class Student(models.Model):
    """Model Student"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name='Carrera del estudiante')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
