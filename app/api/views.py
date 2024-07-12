from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from storage.models import CodeStorage
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@require_http_methods(["GET"])
def explore(request):
    storages = CodeStorage.most_recent()

    formatted_data = []
    for storage in storages:
        formatted_data.append({
            'slug': storage.slug,
            'title': storage.title,
            'creation': storage.created.strftime("%H:%M %d/%m")
        })

    return JsonResponse({'data': formatted_data})

@csrf_exempt
@require_http_methods(["GET", "POST"])
def storage(request):
    if request.method == 'GET':
        slug = request.GET.get('slug')
        password = request.GET.get('password', None)
        storage = CodeStorage.search_by_slug(slug, password=password)
        if storage:
            storage.increase_view()
            data = {
                'creation': storage.created.strftime("%H:%M %d/%m"),
                'title': storage.title,
                'content': storage.content,
                'views': storage.views
            }
            return JsonResponse(data)

    elif request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        password = data.get('password', None)
        
        if not all([title, content]):
            return JsonResponse({'error': 'Campos obrigatórios ausentes'}, status=400)

        result = CodeStorage.create_storage(title, content, password)
        if result:
            return JsonResponse({'slug': result.slug, 'message': 'Dados salvos com sucesso'}, status=201)
        return JsonResponse({'error': 'Problema ao criar registro'}, status=500)