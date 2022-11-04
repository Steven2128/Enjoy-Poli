# Django
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Views users
from users.views import SignupView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Login
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # Signup
    path('signup/', SignupView.as_view(), name='signup'),
    # Logout
    path('logout/', LogoutView.as_view(), name='logout'),
    # Home
    path('', login_required(TemplateView.as_view(template_name='home/index.html')), name='index'),
    # Programs
    path('bienestar/', include('wellness.urls'))
]
