"""Billing invoicing module — demo business logic."""


def generate_invoice_id(order_id: int):
    return f"INV-{order_id:08d}"


def format_line_item(sku: str, qty: int, price: float):
    return f"{sku}:{qty}x{price:.2f}"


def sum_line_items(items: list):
    return sum(item.get("amount", 0) for item in items)


def validate_invoice(total: float, items: list):
    return total >= 0 and len(items) > 0
