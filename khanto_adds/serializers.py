from rest_framework import serializers

from khanto_adds.models import Imovel, Anuncio


class ImovelUpdateOrCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        exclude = [
            "is_active",
        ]


class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = "__all__"


class AnuncioUpdateOrCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        exclude = [
            "is_active",
        ]


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = "__all__"
