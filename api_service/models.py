from django.db import models
from django.utils import timezone
from utils.id_generators.manager import IDManager
from django.conf import settings


class ShortURL(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        default=IDManager.generate_id,
        editable=False,
    )
    long_url = models.URLField(max_length=2048)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    short_code = models.CharField(max_length=15, unique=True)
    click_count = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["short_code"]),
        ]

    @property
    def short_url(self) -> str:
        return f"{settings}/{self.short_code}"

    def is_expired(self) -> bool:
        return self.expires_at and self.expires_at <= timezone.now()
