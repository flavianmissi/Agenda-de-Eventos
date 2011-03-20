#-*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from models import ItemAgenda
from forms import FormItemAgenda

def lista(request):
    lista_itens = ItemAgenda.objects.all()
    return render_to_response('lista.html', { 'lista_itens':lista_itens }, context_instance=RequestContext(request))

def adiciona(request):
    if request.method == "POST":
        form = FormItemAgenda(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            item = ItemAgenda(data=dados['data'], hora=dados['hora'], titulo=dados['titulo'], descricao=dados['descricao'])
            item.save()
            messages.add_message(request, messages.INFO, 'Item salvo com sucesso')
            return HttpResponseRedirect("/")
        else:
            return render_to_response('adiciona.html', { 'form':form }, context_instance=RequestContext(request))
    else:
        form = FormItemAgenda()
        return render_to_response('adiciona.html', { 'form':form }, context_instance=RequestContext(request))

def item(request, item_id):
    item = get_object_or_404(ItemAgenda, pk=item_id)
    return render_to_response('item.html', {'item':item})


def remove(request, item_id):
    item = ItemAgenda.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect("/")
