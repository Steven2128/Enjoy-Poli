# Django
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
# Models
from .models import Student
# Models wellness
from wellness.models import Career


class SignupForm(forms.ModelForm):
    """Form Signup"""
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    career = forms.ModelChoiceField(queryset=Career.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'career', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            # Verifica si ya existe un usuario con ese email
            raise ValidationError({'email': ["Ya existe un usuario con ese correo"]})
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            career = self.cleaned_data.get('career')
            Student.objects.create(user=user, career=career)
        return user


