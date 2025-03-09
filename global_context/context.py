from typing import Any

_global_context = {
    "TOKEN": "sldkjfsadlgkjalkdgj"
}

def save_to_context(key: str, value: Any):
    _global_context[key] = value

def get_from_context(key: str) -> Any:
    return _global_context.get(key, None)