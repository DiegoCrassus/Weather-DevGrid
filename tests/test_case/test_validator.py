from functools import wraps
from unittest.mock import MagicMock

def mock_if_testing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if getattr(args[0], 'testing', True):
            return MagicMock()
        else:
            return func(*args, **kwargs)
    return wrapper