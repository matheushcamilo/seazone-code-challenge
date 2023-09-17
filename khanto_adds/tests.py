from django.test import TestCase
from .models import Imovel, Anuncio, Reserva


class BaseTestCase(TestCase):
    def setUp(self):
        self.imovel = Imovel.objects.create(
            limite_de_hospedes=5,
            quantidade_de_banheiros=2,
            quantidade_de_quartos=3,
            aceita_animais=True,
            valor_da_limpeza=100.00,
            data_de_ativacao='2023-09-17'
        )
        self.anuncio = Anuncio.objects.create(
            imovel=self.imovel,
            plataforma_de_anuncio='Airbnb',
            taxa_da_plataforma=10.00
        )
        self.reserva = Reserva.objects.create(
            anuncio=self.anuncio,
            data_de_checkin='2023-09-20',
            data_de_checkout='2023-09-25',
            preco_total=110.00,
            numero_de_hospedes=3
        )


class ImovelTestCase(BaseTestCase):
    def test_codigo_generation(self):
        # Ensure a unique code is generated for each Imovel object
        self.assertIsNotNone(self.imovel.codigo)

    def test_str_method(self):
        # Ensure the __str__ method returns the expected string
        expected_str = self.imovel.codigo
        self.assertEqual(str(self.imovel), expected_str)


class AnuncioTestCase(BaseTestCase):
    def test_str_method(self):
        # Ensure the __str__ method returns the expected string
        expected_str = f"{self.imovel.codigo} - Airbnb"
        self.assertEqual(str(self.anuncio), expected_str)


class ReservaTestCase(BaseTestCase):

    def test_codigo_generation(self):
        self.assertIsNotNone(self.reserva.codigo)

    def test_calcular_preco_total(self):
        # Ensure the calculated total price is correct
        expected_total_price = self.anuncio.taxa_da_plataforma + self.anuncio.imovel.valor_da_limpeza
        self.assertEqual(self.reserva.calcular_preco_total(), expected_total_price)

    def test_str_method(self):
        expected_str = f"{self.anuncio.imovel.codigo} - Airbnb - 2023-09-20 - 2023-09-25"
        self.assertEqual(str(self.reserva), expected_str)
