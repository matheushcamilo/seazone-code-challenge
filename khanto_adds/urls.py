from django.urls import path
from khanto_adds.apis import ImovelApiView, ImovelRetrieveApiView

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
    )
]
