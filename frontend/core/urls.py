"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import LoginView, check_name, getHome, getLogin, getEmployeeHome, getManagerHome
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee/login/', LoginView.as_view(), name='login_view'),
    path('check_name/', check_name, name='check_name'),
    path('home/', getHome, name='getHome'),
    path('employee/home', getEmployeeHome, name='getEmployeeHome'),
    path('manager/home', getManagerHome, name='getManagerHome'),
    path('login/', getLogin, name='getLogin')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
