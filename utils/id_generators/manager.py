from utils.id_generators.snowflake_generator import SnowflakeIDGenerator
from utils.encode_base62 import Base62Encoder
from utils.log import get_logger

logger = get_logger("utils.id_generator.manager")

class IDManager:
    """
    Stable ID generation interface.
    """

    @staticmethod
    def generate_id() -> int:
        raw_id = SnowflakeIDGenerator.generate_id()
        logger.debug(f"Generated raw ID: {raw_id}")
        return raw_id

    @staticmethod
    def encode_id(raw_id: int) -> str:
        encoded = Base62Encoder.encode(raw_id)
        logger.debug(
            "Encoded ID",
            extra={"raw_id": raw_id, "encoded_id": encoded},
        )
        return encoded

    @classmethod
    def generate_encoded_id(cls) -> str:
        raw_id = cls.generate_id()
        encoded = cls.encode_id(raw_id)
        logger.info(f"Generated encoded ID: {encoded}")
        return encoded


if __name__ == "__main__":
    gen = IDManager()
    new_id = gen.generate_encoded_id()
    print("encoded_new_id ", new_id)