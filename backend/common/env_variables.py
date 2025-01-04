import os
from typing import Any


def get_env_variable(key: str, required=False) -> Any:
    value = os.getenv(key)
    if value is None and required:
        raise ValueError(f"Environment variable {key} is missing.")
    return value
