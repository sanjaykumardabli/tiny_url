from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from django.utils import timezone

from utils.id_generators.manager import IDManager
from .serializers import ShortURLCreateSerializer, ShortCodeSerializer
from .models import ShortURL
from .services import get_long_url_by_short_code
from utils.exceptions.shortner import (
    ShortURLNotFound,
    ShortURLExpired,
)

class ShortenURLAPIView(APIView):
    """
    Create a short URL with optional expiry.
    """

    def post(self, request):
        serializer = ShortURLCreateSerializer(
            data=request.data,
        )

        if serializer.is_valid(raise_exception=True):
            long_url = serializer.validated_data.get("long_url")
            short_code = IDManager.generate_encoded_id()
            short_url_obj = ShortURL.objects.create(
                short_code=short_code,
                long_url=long_url
            )

            return Response(
                {
                    "short_code": short_url_obj.short_code,
                    "long_url": short_url_obj.long_url,
                    "expires_at": short_url_obj.expires_at,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectAPIView(APIView):
    """
    Redirect short code → original/long URL.
    """

    def get(self, request, short_code):
        serializer = ShortCodeSerializer(
            data={"short_code": short_code},
        )
        if serializer.is_valid(raise_exception=True):
            try:
                long_url = get_long_url_by_short_code(short_code)
                return HttpResponseRedirect(long_url)
            except ShortURLNotFound as exc:
                return Response(
                    {"detail": str(exc)},
                    status=status.HTTP_404_NOT_FOUND,
                )
            except ShortURLExpired as exc:
                return Response(
                    {"detail": str(exc)},
                    status=status.HTTP_410_GONE,
                )

