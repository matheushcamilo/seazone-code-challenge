from django.contrib import admin
from khanto_adds.models import Imovel, Anuncio, Reserva


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    model = Imovel
    list_display = (
        "codigo",
        "limite_de_hospedes",
        "quantidade_de_banheiros",
        "quantidade_de_quartos",
        "aceita_animais",
        "valor_da_limpeza",
        "data_de_ativacao",
        "is_active",
    )
    list_filter = (
        "aceita_animais",
        "quantidade_de_banheiros",
        "quantidade_de_quartos",
        "limite_de_hospedes",
        "is_active",
    )
    date_hierarchy = "data_de_ativacao"


@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    model = Anuncio
    list_display = (
        "imovel",
        "plataforma_de_anuncio",
        "taxa_da_plataforma",
        "is_active",
    )
    list_filter = (
        "plataforma_de_anuncio",
        "is_active",
    )
    search_fields = (
        "imovel__codigo",
    )
    raw_id_fields = ["imovel"]


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    model = Reserva
    readonly_fields = ["codigo", "preco_total"]
    list_display = (
        "anuncio",
        "data_de_checkin",
        "data_de_checkout",
        "preco_total",
        "numero_de_hospedes",
        "is_active",
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "imovel__codigo",
    )
    raw_id_fields = ["anuncio"]
