from django.shortcuts import render, HttpResponse
from storage.models import CodeStorage

# Create your views here.

def search(request, slug):
    password = request.GET.get('password', None)
    storage = CodeStorage.search_by_slug(slug, password=password)
    if storage:
        storage.increase_view()
        return HttpResponse(storage.content)
    else:
        return HttpResponse("Conteudo nao encontrado.")