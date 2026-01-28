from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import ShortURL

from utils.exceptions.shortner import (
    ShortURLNotFound,
    ShortURLExpired,
)

def get_long_url_by_short_code(short_code: str) -> ShortURL:
    """
    Decode short code and return active ShortURL.
    """
    try:
        short_url_obj = ShortURL.objects.get(short_code=short_code)
        if short_url_obj.expires_at and short_url_obj.expires_at <= timezone.now():
                raise ShortURLExpired("URL has expired")

        return short_url_obj.long_url
    except:
        raise ShortURLNotFound("Short URL not found")
