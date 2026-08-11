"""Inventory warehouse module — demo business logic."""

def assign_bin(warehouse: str, aisle: int, slot: int):
    return f"{warehouse}-{aisle}-{slot}"

def locate_item(sku: str):
    return f"BIN-{sku}" if sku else None

def transfer_stock(source_qty: int, qty: int):
    return source_qty - qty if source_qty >= qty else 0

def warehouse_capacity(capacity: int, used: int):
    return max(0, capacity - used)
