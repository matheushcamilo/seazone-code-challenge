from django.urls import path
from khanto_adds.apis import (
    ImovelApiView,
    ImovelUpdateDestroyApiView,
    AnuncioApiView,
    AnuncioUpdateApiView,
    ReservaApiView,
    ReservaDestroyApiView
)

urlpatterns = [
    path(
        "imoveis/",
        ImovelApiView.as_view(),
        name="imovel-api"
    ),
    path(
        "imoveis/<int:imovel_id>/",
        ImovelUpdateDestroyApiView.as_view(),
        name="imovel-by-id"
    ),
    path(
        "anuncios/",
        AnuncioApiView.as_view(),
        name="anuncio-api"
    ),
    path(
        "anuncios/<int:anuncio_id>/",
        AnuncioUpdateApiView.as_view(),
        name="anuncio-by-id"
    ),
    path(
        "reservas/",
        ReservaApiView.as_view(),
        name="reserva-api"
    ),
    path(
        "reservas/<int:reserva_id>/",
        ReservaDestroyApiView.as_view(),
        name="reserva-by-id"
    ),
]
