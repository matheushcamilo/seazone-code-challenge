from django.urls import path
from khanto_adds.apis import ImovelApiView, ImovelRetrieveApiView, AnuncioApiView, AnuncioRetrieveApiView

urlpatterns = [
    path(
        "imoveis/",
        ImovelApiView.as_view(),
        name="imovel-api"
    ),
    path(
        "imoveis/<int:imovel_id>/",
        ImovelRetrieveApiView.as_view(),
        name="imovel-by-id"
    ),
    path(
        "anuncios/",
        AnuncioApiView.as_view(),
        name="anuncio-api"
    ),
    path(
        "anuncios/<int:anuncio_id>/",
        AnuncioRetrieveApiView.as_view(),
        name="anuncio-by-id"
    ),
]
