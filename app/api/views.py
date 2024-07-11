from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from storage.models import CodeStorage

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

