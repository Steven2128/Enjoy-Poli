# Django
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


class Program(models.Model):
    """Model Program"""
    ACTIVITY_IN_PROGRAM_CHOICES = [
        ('AC', 'ACTIVIDADES CULTURALES'),
        ('AD', 'ACTIVIDADES DEPORTIVAS'),
        ('CME', 'CONSULTA MÉDICA Y ENFERMERÍA'),
        ('SP', 'SEMILLITAS POLI'),
    ]
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre del programa')
    description = models.CharField(max_length=150, blank=False, null=False, verbose_name='Descripción del programa')
    capacity = models.PositiveIntegerField(verbose_name='Cupo del programa')
    current_capacity_available = models.PositiveIntegerField(blank=True, null=True, default=0, validators=[], verbose_name='Cupo actual disponible del programa')
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Fecha inicio del programa')
    final_data = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Fecha inicio del programa')
    status = models.BooleanField(default=True, verbose_name='Estado del programa')
    image = models.ImageField(default='sample.jpg', upload_to='programs', verbose_name='Imagen del programa')
    activity = models.CharField(max_length=3, choices=ACTIVITY_IN_PROGRAM_CHOICES, blank=False, null=False, verbose_name='Actividad del programa')
    users = models.ManyToManyField(User, blank=True, verbose_name='Usuario relacionado al programa')

    def __str__(self):
        return "{} - Duración: {} hasta {} - Cupo actual: {} - Estudiantes: {}".format(self.name, self.start_date, self.final_data, self.current_capacity_available, self.users.count())

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'


class Assistance(models.Model):
    date_assistance = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha asistencia')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Programa relacionado a la asistencia')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario relacionado a la asistencia')

    def __str__(self):
        return "Asistencia: {} - Estudiante: {} - Fecha: {}".format(self.program.name, self.user.get_full_name(), self.date_assistance)

    def save(self):
        # const = Assistance.objects.filter(programs__in=[prom])
        # const = Assistance.objects.filter(programs=[self.programs]).filter(user=[self.user])
        super(Assistance, self).save()

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'


