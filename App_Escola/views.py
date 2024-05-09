from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import PessoaForm
from .models import Pessoa
from django.http import HttpResponseRedirect


def inserir_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'inserir_pessoa.html', {'form': form})

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'lista_pessoas.html', {'pessoas': pessoas})

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def excluir_pessoa(request, pessoa_id):
    try:
        pessoa = Pessoa.objects.get(pk=pessoa_id)
    except Pessoa.DoesNotExist:
        raise Http404("Pessoa não encontrada")
    
    pessoa.delete()
    return redirect('lista_pessoas')

def editar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/lista/')  # Redirecionar para a página de lista após a edição
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'editar_pessoa.html', {'form': form})
