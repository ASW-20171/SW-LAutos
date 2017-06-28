from rest_framework import serializers, viewsets
from ..models.Reserva import Reserva


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        # fiels


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
