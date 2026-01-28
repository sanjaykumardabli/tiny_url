import re

from rest_framework import serializers


class ShortURLCreateSerializer(serializers.Serializer):
    long_url = serializers.CharField(required=True)

class ShortCodeSerializer(serializers.Serializer):
    short_code = serializers.CharField(
        trim_whitespace=True,
    )

    def validate_short_code(self, value: str) -> str:
        if not re.fullmatch(r"[0-9A-Za-z]+", value) or not 10 <= len(value) <= 15:
            raise serializers.ValidationError(
                "Invalid short code format"
            )
        return value

class IDResponseSerializer(serializers.Serializer):
    short_code = serializers.CharField(read_only=True)
    long_url = serializers.URLField(read_only=True)
    created_at = serializers.DateTimeField()
