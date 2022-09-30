# Django
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Logout
    path('logout/', LogoutView.as_view(), name='logout'),
    # Home
    path('', TemplateView.as_view(template_name='home/index.html'), name='index'),
    # Programs
    path('bienestar/', include('wellness.urls'))
]
