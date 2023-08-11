"""
URL configuration for project14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('box/', box, name = 'box'),
    path('me', me, name = 'me'),
    path('fourimages/', fourimages, name='fourimages'),
    path('imagehandling/', imagehandling, name = 'imagehandling'),
    path('random/', random, name = 'random'),
    path('seminar/', seminar, name = 'seminar'),
    path('student/', student, name='student'),
    path('transform/', transform, name='trnasform'),
    path('bubbles/', bubbles, name='bubbles'),
    path('application/', application, name='application'),
    path('birthday/', birthday, name='birthday'),
]
