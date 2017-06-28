from django.conf.urls import url, include
from rest_framework import routers
from reserva.view.ReservaView import ReservaViewSet


router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
