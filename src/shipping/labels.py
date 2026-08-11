"""Shipping labels module — demo business logic."""


def generate_label(order_id: int):
    return f"LBL-{order_id}"


def validate_address(street: str, city: str, zip_code: str):
    return bool(street and city and zip_code)


def package_dimensions(length: float, width: float, height: float):
    return length * width * height


def label_format(international: bool):
    return "PDF" if international else "ZPL"
