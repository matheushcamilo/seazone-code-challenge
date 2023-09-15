from rest_framework import generics

from khanto_adds.serializers import ImovelSerializer, ImovelUpdateOrCreateSerializer
from khanto_adds.models import Imovel


class ImovelApiView(generics.ListCreateAPIView):
    queryset = Imovel.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ImovelUpdateOrCreateSerializer
        else:
            return ImovelSerializer


class ImovelRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "imovel_id"
    queryset = Imovel.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ImovelUpdateOrCreateSerializer
        else:
            return ImovelSerializer
