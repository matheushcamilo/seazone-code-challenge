from rest_framework import serializers

from khanto_adds.models import Imovel, Anuncio, Reserva


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


class ReservaCreateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs["data_de_checkin"] > attrs["data_de_checkout"]:
            raise serializers.ValidationError(
                "Data de checkin não pode ser maior que a data de checkout"
            )
        return attrs

    class Meta:
        model = Reserva
        exclude = [
            "is_active",
        ]
        read_only_fields = [
            "codigo",
            "preco_total",
        ]


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"
