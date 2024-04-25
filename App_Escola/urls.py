from . import views
from django.urls import path

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('login/', views.enviar_login, name='enviar_login'),
    path('confirmar_cadastro/', views.confirmar_cadastro, name='confirmar_cadastro'),
    path('cad_turma/<int:id_professor>', views.cad_turma, name='cad_turma'),
    #Rota para salvar uma nova turma
    path('salvar_turma/', views.salvar_turma_nova, name='salvar_turma_nova'),
    path('lista_turma/<int:id_professor>', views.lista_turma, name='lista_turma'),
    path('ver_atividades/', views.ver_atividades, name='ver_atividades'),
    #Rota para salvar uma nova atividade
    path('salvar_atividade/', views.salvar_atividade_nova, name='salvar_atividade_nova'),
    #Rota para excluir uma turma
    path('excluir_turma/<int:id_turma>', views.excluir_turma, name='excluir_turma')
]
