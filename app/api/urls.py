from django.urls import path
from api.views import explore, storage

urlpatterns = [
    path('explore/', explore),
    path('storage/', storage),
]