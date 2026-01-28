from django.conf import settings
from snowflake import SnowflakeGenerator
from django.core.exceptions import ImproperlyConfigured


class SnowflakeIDGenerator:
    _generator = None

    @classmethod
    def _init_generator(cls):
        if cls._generator is not None:
            return

        instance_id = getattr(settings, "SNOWFLAKE_INSTANCE_ID", 1)

        if instance_id is None:
            raise ImproperlyConfigured(
                "INSTANCE_ID environment variable is not set"
            )

        try:
            instance_id = int(instance_id)
        except ValueError:
            raise ImproperlyConfigured(
                "INSTANCE_ID must be an integer"
            )

        if not (0 <= instance_id <= 1023):
            raise ImproperlyConfigured(
                "INSTANCE_ID must be between 0 and 1023"
            )

        cls._generator = SnowflakeGenerator(instance_id)

    @classmethod
    def generate_id(cls) -> int:
        cls._init_generator()
        return next(cls._generator)

if __name__ == "__main__":
    ids = [SnowflakeIDGenerator.generate() for _ in range(10)]
    breakpoint()
    print(ids)