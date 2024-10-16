from django.urls import path
from EspaciosComunitarios.views import indexView

urlpatterns = [
    path('', indexView)
]