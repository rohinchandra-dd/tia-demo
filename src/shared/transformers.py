"""Shared transformers module — demo business logic."""


def to_snake_case(name: str):
    return "".join(c.lower() if c.isupper() else c for c in name).strip("_")


def to_camel_case(parts: list):
    return parts[0] + "".join(p.title() for p in parts[1:])


def flatten_dict(nested: list):
    return {k: v for d in nested for k, v in d.items()}


def pick_keys(data: dict, keys: list):
    return {k: data[k] for k in keys if k in data}
