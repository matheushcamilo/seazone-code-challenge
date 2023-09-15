from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from khanto_adds.serializers import (
    ImovelSerializer,
    ImovelUpdateOrCreateSerializer,
    AnuncioSerializer,
    AnuncioUpdateOrCreateSerializer,
    ReservaSerializer,
    ReservaCreateSerializer,
)
from khanto_adds.models import Imovel, Anuncio, Reserva


class ImovelApiView(generics.ListCreateAPIView):
    queryset = Imovel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ImovelUpdateOrCreateSerializer
        else:
            return ImovelSerializer


class ImovelUpdateDestroyApiView(generics.UpdateAPIView, generics.DestroyAPIView):
    lookup_url_kwarg = "imovel_id"
    queryset = Imovel.objects.all()
    serializer_class = ImovelUpdateOrCreateSerializer


class AnuncioApiView(generics.ListCreateAPIView):
    queryset = Anuncio.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AnuncioUpdateOrCreateSerializer
        else:
            return AnuncioSerializer


class AnuncioUpdateApiView(generics.UpdateAPIView):
    lookup_url_kwarg = "anuncio_id"
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioUpdateOrCreateSerializer


class ReservaApiView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ReservaCreateSerializer
        else:
            return ReservaSerializer


class ReservaDestroyApiView(generics.DestroyAPIView):
    lookup_url_kwarg = "reserva_id"
    queryset = Reserva.objects.all()
