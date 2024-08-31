# urls.py | Employee Service
from django.contrib import admin
from django.urls import path
from employees.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee/login/', LoginView.as_view(), name='login'),
]
