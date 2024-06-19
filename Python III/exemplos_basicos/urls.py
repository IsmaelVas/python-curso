from django.urls import path
from . import views

# Informado quais serão as rotas do nosso app exemplos_basicos
urlpatterns = [
    # Quando a rota exemplos-basicos/home for acessada irá executar o código da função home do arquivo views.py
    path("/home", views.index),
    path("/", views.index),
    path("/contato", views.contato),
    path("/jogo", views.jogo),
    path("/calculadora", views.calculadora),
    path("/calculadora/numero1/<int:numero1>", views.calculadora),
    path("/calculadora/numero2/<int:numero2>", views.calculadora),
    path("/calculadora/numero1/<int:numero1>/numero2/<int:numero2>", views.calculadora),
    path("/calculadora-form", views.calculadora_form),
    path("/calcular", views.calcular),
    path("/sobre", views.sobre),
    path("/sobre-form", views.sobre_form),
    path("/mandar", views.mandar),
    path("/cadastro-carro-form", views.cadastro_carro)
    ]