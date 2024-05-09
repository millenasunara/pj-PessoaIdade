from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inserir_pessoa, name='pagina_inicial'),  # Redireciona para a página de inserção de pessoas
    path('inserir/', views.inserir_pessoa, name='inserir_pessoa'),
    path('lista/', views.lista_pessoas, name='lista_pessoas'),
    path('excluir/<int:pessoa_id>/', views.excluir_pessoa, name='excluir_pessoa'),
    path('editar/<int:pessoa_id>/', views.editar_pessoa, name='editar_pessoa')  # Importe a função editar_pessoa de views.py
]
