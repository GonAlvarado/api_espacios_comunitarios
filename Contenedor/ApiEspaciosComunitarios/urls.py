from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from .views import(
    EspacioViewSet,
    DiaViewSet,
    HorarioViewSet,
    ReferenteViewSet,
    RetiroViewSet,
    login
)

router = DefaultRouter()
router.register('espacios', EspacioViewSet, basename='espacios')
router.register('dias', DiaViewSet, basename='dias')
router.register('horarios', HorarioViewSet, basename='horarios')
router.register('referentes', ReferenteViewSet, basename='referentes')
router.register('retiros', RetiroViewSet, basename='retiros')

urlpatterns = [
    re_path('login', login),
]

urlpatterns += router.urls