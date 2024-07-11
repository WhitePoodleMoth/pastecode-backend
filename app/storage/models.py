from django.db import models

# Create your models here.

class CodeStorage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiration = models.DateTimeField(null=True, blank=True)
    slug = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=25000)
    password = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)

    @classmethod
    def search_by_slug(cls, slug):
        try:
            return cls.objects.get(slug=slug)
        except:
            return False