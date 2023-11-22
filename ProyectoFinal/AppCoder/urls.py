from django.urls import path
from django.http import HttpResponse

from AppCoder.views import inicio_view, cursos_view

urlpatterns = [
  path("inicio/", inicio_view),
  path("cursos/", cursos_view),
]