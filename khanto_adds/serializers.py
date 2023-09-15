from rest_framework import serializers

from khanto_adds.models import Imovel


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
