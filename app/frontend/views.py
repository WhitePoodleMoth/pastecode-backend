from django.shortcuts import render, HttpResponse
from storage.models import CodeStorage

# Create your views here.

def search(request, slug):
    storage = CodeStorage.search_by_slug(slug)
    if storage:
        return HttpResponse(storage.content)
    else:
        return HttpResponse("Conteudo nao encontrado.")