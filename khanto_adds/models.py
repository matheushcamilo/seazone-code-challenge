from django.db import models
import string
import random


class TimeStampActiveMixin(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GeradorDeCodigoMixin(models.Model):
    codigo = models.CharField(max_length=10, unique=True, blank=True)

    class Meta:
        abstract = True

    def gerar_codigo(self):
        characters = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(characters) for _ in range(6))
        while self.__class__.objects.filter(codigo=code).exists():
            code = ''.join(random.choice(characters) for _ in range(6))
        return code


class Imovel(TimeStampActiveMixin, GeradorDeCodigoMixin):
    limite_de_hospedes = models.PositiveSmallIntegerField()
    quantidade_de_banheiros = models.PositiveSmallIntegerField()
    quantidade_de_quartos = models.PositiveSmallIntegerField()
    aceita_animais = models.BooleanField(default=False)
    valor_da_limpeza = models.DecimalField(max_digits=10, decimal_places=2)
    data_de_ativacao = models.DateField()

    def __str__(self):
        return self.codigo

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = self.gerar_codigo()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'


class Anuncio(TimeStampActiveMixin):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    plataforma_de_anuncio = models.CharField(max_length=50)
    taxa_da_plataforma = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.imovel.codigo} - {self.plataforma_de_anuncio}"

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'


class Reserva(TimeStampActiveMixin, GeradorDeCodigoMixin):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    data_de_checkin = models.DateField()
    data_de_checkout = models.DateField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    numero_de_hospedes = models.PositiveSmallIntegerField()

    def __str__(self):
        return (f"{self.anuncio.imovel.codigo} - {self.anuncio.plataforma_de_anuncio}"
                f" - {self.data_de_checkin} - {self.data_de_checkout}")

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = self.gerar_codigo()

        self.preco_total = self.calcular_preco_total()

        super().save(*args, **kwargs)

    def calcular_preco_total(self):
        return self.anuncio.taxa_da_plataforma + self.anuncio.imovel.valor_da_limpeza

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

