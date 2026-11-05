"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    result = int(value.strip())
    if result < 1:
        raise ValueError(f"quantity must be positive, got {result}")
    return result
