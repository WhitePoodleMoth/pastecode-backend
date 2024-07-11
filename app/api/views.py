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

