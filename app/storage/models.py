from django.db import models
from django.utils import timezone
from django.db.models import Q

# Create your models here.

class CodeStorage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiration = models.DateTimeField(null=True, blank=True)
    slug = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=25000)
    password = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    @classmethod
    def most_recent(cls, amount=10):
        now = timezone.now()
        return cls.objects.filter(
            Q(expiration__isnull=True) | Q(expiration__gt=now),
            active=True,
            password=None,
        ).order_by('-created')[:amount]

    @classmethod
    def search_by_slug(cls, slug, password=None):
        try:
            storage = cls.objects.get(slug=slug)
            if not storage.active:
                raise Exception
            if storage.expiration is not None and timezone.now() > storage.expiration:
                raise Exception
            if storage.password and password!=storage.password:
                raise Exception
            return storage
        except:
            return False
    
    def increase_view(self):
        self.views = self.views + 1
        self.save()