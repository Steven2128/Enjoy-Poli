# Django
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Faculty(models.Model):
    """Model Faculty"""
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name='Nombre de la facultad')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'


class Career(models.Model):
    """Model Career"""
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name='Nombre de la carrera')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Facultad a la que pertenece la carrera')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'


class Program(models.Model):
    """Model Program"""
    ACTIVITY_IN_PROGRAM_CHOICES = [
        ('AC', 'ACTIVIDADES CULTURALES'),
        ('AD', 'ACTIVIDADES DEPORTIVAS'),
        ('CME', 'CONSULTA MÉDICA Y ENFERMERÍA'),
        ('SP', 'SEMILLITAS POLI'),
    ]
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre del programa')
    description = models.TextField(blank=False, null=False, verbose_name='Descripción del programa')
    capacity = models.PositiveIntegerField(verbose_name='Cupo del programa')
    current_capacity_available = models.PositiveIntegerField(blank=True, null=True, default=0, validators=[], verbose_name='Cupo actual disponible del programa')
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE, verbose_name='Profesor asignado al programa')
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Fecha inicio del programa')
    final_data = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Fecha inicio del programa')
    status = models.BooleanField(default=True, verbose_name='Estado del programa')
    image = models.URLField(default='sample.jpg', verbose_name='Ruta de la imagen del programa')
    activity = models.CharField(max_length=3, choices=ACTIVITY_IN_PROGRAM_CHOICES, blank=False, null=False, verbose_name='Actividad del programa')
    students = models.ManyToManyField("users.Student", blank=True, verbose_name='Estudiantes relacionado al programa')
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{} - Duración: {} hasta {} - Cupo actual: {} - Estudiantes: {}".format(self.name, self.start_date, self.final_data, self.current_capacity_available, self.students.count())

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Program, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def get_absolute_url(self):
        return reverse("program_detail", kwargs={"slug": self.slug})


class Assistance(models.Model):
    """Model Assistance"""
    date_assistance = models.DateField(auto_now_add=True, auto_now=False, verbose_name='Fecha asistencia')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Programa de la asistencia')
    student = models.ForeignKey("users.Student", on_delete=models.CASCADE, verbose_name='Estudiante')

    def __str__(self):
        return "Asistencia: {} - Programa: {} - Estudiante: {}".format(self.date_assistance, self.program.name, self.student.get_full_name())

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'


class Schedule(models.Model):
    """Model Schedule"""
    DAYS_OF_WEEK = (
        ('0', 'Domingo'),
        ('1', 'Lunes'),
        ('2', 'Martes'),
        ('3', 'Miercoles'),
        ('4', 'Jueves'),
        ('5', 'Viernes'),
        ('6', 'Sabado'),
    )
    day = models.CharField(max_length=3, blank=False, null=False, choices=DAYS_OF_WEEK, verbose_name='Día de la clase')
    start_time = models.TimeField(blank=False, null=False, verbose_name='Hora inicio clase')
    final_time = models.TimeField(blank=False, null=False, verbose_name='Hora final clase')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Programa de la clase')

    def __str__(self):
        return "Programa: {} - Día: {} {}/{} - ".format(self.program.name, self.day, self.start_time, self.final_time)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

