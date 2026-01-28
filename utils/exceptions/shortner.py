class ShortURLNotFound(Exception):
    """
    Raised when short code does not exist.
    """
    pass


class ShortURLExpired(Exception):
    """
    Raised when short URL is expired.
    """
    pass
