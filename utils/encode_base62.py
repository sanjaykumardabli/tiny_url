import string


class Base62Encoder:
    _alphabet = string.digits + string.ascii_letters
    _base = len(_alphabet)

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError("Number must be non-negative")

        if num == 0:
            return cls._alphabet[0]

        encoded = []
        while num:
            num, rem = divmod(num, cls._base)
            encoded.append(cls._alphabet[rem])

        return ''.join(reversed(encoded))
