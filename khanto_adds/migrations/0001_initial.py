# Generated by Django 4.2.5 on 2023-09-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Anuncio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("plataforma_de_anuncio", models.CharField(max_length=50)),
                (
                    "taxa_da_plataforma",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
            options={
                "verbose_name": "Anúncio",
                "verbose_name_plural": "Anúncios",
            },
        ),
        migrations.CreateModel(
            name="Imovel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("codigo", models.CharField(blank=True, max_length=10, unique=True)),
                ("limite_de_hospedes", models.PositiveSmallIntegerField()),
                ("quantidade_de_banheiros", models.PositiveSmallIntegerField()),
                ("quantidade_de_quartos", models.PositiveSmallIntegerField()),
                ("aceita_animais", models.BooleanField(default=False)),
                (
                    "valor_da_limpeza",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("data_de_ativacao", models.DateField()),
            ],
            options={
                "verbose_name": "Imóvel",
                "verbose_name_plural": "Imóveis",
            },
        ),
        migrations.CreateModel(
            name="Reserva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("codigo", models.CharField(blank=True, max_length=10, unique=True)),
                ("data_de_checkin", models.DateField()),
                ("data_de_checkout", models.DateField()),
                ("preco_total", models.DecimalField(decimal_places=2, max_digits=10)),
                ("comentario", models.TextField(blank=True, null=True)),
                ("numero_de_hospedes", models.PositiveSmallIntegerField()),
                (
                    "anuncio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="khanto_adds.anuncio",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reserva",
                "verbose_name_plural": "Reservas",
            },
        ),
        migrations.AddField(
            model_name="anuncio",
            name="imovel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="khanto_adds.imovel"
            ),
        ),
    ]