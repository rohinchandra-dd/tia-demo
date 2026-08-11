#!/usr/bin/env python3
"""Generate src modules and pytest test files from domain_spec.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "scripts" / "domain_spec.json"

HEAVY_PARAM_COUNT = 18
LIGHT_PARAM_COUNT = 6
HEAVY_FUNCTIONS = 4
LIGHT_FUNCTIONS = 2


def load_spec() -> dict:
    with SPEC_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def op_impl(op: str) -> str:
    """Return a simple pure-function body for an operation."""
    templates = {
        "add_tax": "return round(amount * (1 + rate), 2)",
        "apply_discount": "return max(0.0, amount - discount)",
        "round_currency": "return round(value, decimals)",
        "split_payment": "return round(total / parts, 2)",
        "generate_invoice_id": 'return f"INV-{order_id:08d}"',
        "format_line_item": 'return f"{sku}:{qty}x{price:.2f}"',
        "sum_line_items": "return sum(item.get('amount', 0) for item in items)",
        "validate_invoice": "return total >= 0 and len(items) > 0",
        "apply_coupon": "return amount * (1 - min(1.0, percent))",
        "tier_discount": "return amount * (1 - tier * 0.05)",
        "bulk_discount": "return amount * (1 - min(0.25, qty * 0.01))",
        "validate_promo": "return len(code) >= 4 and code.isalnum()",
        "calculate_refund": "return min(original, requested)",
        "partial_refund": "return round(original * ratio, 2)",
        "refund_eligible": "return days_since_purchase <= window_days",
        "format_refund": 'return f"REF-{refund_id:06d}"',
        "check_stock": "return available >= requested",
        "reserve_stock": "return max(0, available - requested)",
        "release_stock": "return available + released",
        "stock_level": 'return "low" if qty < threshold else "ok"',
        "assign_bin": 'return f"{warehouse}-{aisle}-{slot}"',
        "locate_item": 'return f"BIN-{sku}" if sku else None',
        "transfer_stock": "return source_qty - qty if source_qty >= qty else 0",
        "warehouse_capacity": "return max(0, capacity - used)",
        "reorder_point": "return avg_daily * lead_days + safety_stock",
        "suggest_quantity": "return max(0, target - on_hand)",
        "lead_time_days": "return max(1, base_days + supplier_delay)",
        "reorder_priority": "return min(10, max(1, urgency // 10))",
        "count_variance": "return abs(expected - actual)",
        "adjust_count": "return actual + adjustment",
        "schedule_count": "return day_of_week in {1, 3, 5}",
        "count_accuracy": "return 1.0 - (variance / max(1, expected))",
        "calculate_rate": "return base + weight * per_kg",
        "zone_rate": "return base * zone_multiplier",
        "weight_tier": "return tier_index * step + base",
        "express_surcharge": "return base * 1.5 if express else base",
        "track_status": 'return status if status in {"shipped", "delivered", "pending"} else "unknown"',
        "eta_estimate": "return days_in_transit + processing_days",
        "format_tracking_id": 'return f"TRK-{tracking_id.upper()}"',
        "delivery_window": 'return f"{start_hour:02d}:00-{end_hour:02d}:00"',
        "generate_label": 'return f"LBL-{order_id}"',
        "validate_address": "return bool(street and city and zip_code)",
        "package_dimensions": "return length * width * height",
        "label_format": 'return "PDF" if international else "ZPL"',
        "select_carrier": 'return carriers[0] if carriers else "default"',
        "carrier_score": "return on_time * 0.6 + cost_score * 0.4",
        "cutoff_time": "return hour < cutoff_hour",
        "service_level": 'return "express" if priority > 5 else "standard"',
        "has_permission": "return permission in role_permissions",
        "merge_roles": "return sorted(set(a) | set(b))",
        "role_hierarchy": "return child_level <= parent_level + 1",
        "permission_mask": "return permissions & mask",
        "generate_token": 'return f"tok_{user_id}_{nonce}"',
        "validate_token": "return token.startswith('tok_') and len(token) > 8",
        "token_expiry": "return issued_at + ttl_seconds",
        "refresh_token": 'return f"ref_{old_token[-8:]}"',
        "create_session": 'return f"sess_{user_id}"',
        "revoke_session": "return session_id not in active",
        "session_ttl": "return max(0, expires_at - now)",
        "active_sessions": "return len([s for s in sessions if s])",
        "generate_otp": "return str(abs(hash(seed)) % 1000000).zfill(6)",
        "verify_otp": "return submitted == expected",
        "backup_codes": "return len(codes) >= min_codes",
        "mfa_required": "return risk_score >= threshold",
        "clamp": "return max(minimum, min(maximum, value))",
        "normalize_email": "return email.strip().lower()",
        "slugify": 'return text.lower().replace(" ", "-")',
        "safe_divide": "return numerator / denominator if denominator else default",
        "is_email": "return '@' in value and '.' in value.split('@')[-1]",
        "is_phone": "return value.isdigit() and 7 <= len(value) <= 15",
        "is_uuid": "return len(value.replace('-', '')) == 32",
        "is_positive": "return value > 0",
        "format_currency": 'return f"${amount:.2f}"',
        "format_date": 'return f"{year:04d}-{month:02d}-{day:02d}"',
        "format_phone": 'return f"({area}) {prefix}-{line}"',
        "truncate_text": "return text[:max_len] + ('...' if len(text) > max_len else '')",
        "to_snake_case": 'return "".join(c.lower() if c.isupper() else c for c in name).strip("_")',
        "to_camel_case": "return parts[0] + ''.join(p.title() for p in parts[1:])",
        "flatten_dict": "return {k: v for d in nested for k, v in d.items()}",
        "pick_keys": "return {k: data[k] for k in keys if k in data}",
    }
    if op in templates:
        return templates[op]
    return f'return int((value * factor + len("{op}")) % 10000)'


def op_signature(op: str) -> str:
    sigs = {
        "add_tax": "amount: float, rate: float",
        "apply_discount": "amount: float, discount: float",
        "round_currency": "value: float, decimals: int = 2",
        "split_payment": "total: float, parts: int",
        "generate_invoice_id": "order_id: int",
        "format_line_item": "sku: str, qty: int, price: float",
        "sum_line_items": "items: list",
        "validate_invoice": "total: float, items: list",
        "apply_coupon": "amount: float, percent: float",
        "tier_discount": "amount: float, tier: int",
        "bulk_discount": "amount: float, qty: int",
        "validate_promo": "code: str",
        "calculate_refund": "original: float, requested: float",
        "partial_refund": "original: float, ratio: float",
        "refund_eligible": "days_since_purchase: int, window_days: int",
        "format_refund": "refund_id: int",
        "check_stock": "available: int, requested: int",
        "reserve_stock": "available: int, requested: int",
        "release_stock": "available: int, released: int",
        "stock_level": "qty: int, threshold: int",
        "assign_bin": "warehouse: str, aisle: int, slot: int",
        "locate_item": "sku: str",
        "transfer_stock": "source_qty: int, qty: int",
        "warehouse_capacity": "capacity: int, used: int",
        "reorder_point": "avg_daily: float, lead_days: int, safety_stock: int",
        "suggest_quantity": "target: int, on_hand: int",
        "lead_time_days": "base_days: int, supplier_delay: int",
        "reorder_priority": "urgency: int",
        "count_variance": "expected: int, actual: int",
        "adjust_count": "actual: int, adjustment: int",
        "schedule_count": "day_of_week: int",
        "count_accuracy": "variance: float, expected: int",
        "calculate_rate": "base: float, weight: float, per_kg: float",
        "zone_rate": "base: float, zone_multiplier: float",
        "weight_tier": "tier_index: int, step: float, base: float",
        "express_surcharge": "base: float, express: bool",
        "track_status": "status: str",
        "eta_estimate": "days_in_transit: int, processing_days: int",
        "format_tracking_id": "tracking_id: str",
        "delivery_window": "start_hour: int, end_hour: int",
        "generate_label": "order_id: int",
        "validate_address": "street: str, city: str, zip_code: str",
        "package_dimensions": "length: float, width: float, height: float",
        "label_format": "international: bool",
        "select_carrier": "carriers: list",
        "carrier_score": "on_time: float, cost_score: float",
        "cutoff_time": "hour: int, cutoff_hour: int",
        "service_level": "priority: int",
        "has_permission": "permission: str, role_permissions: set",
        "merge_roles": "a: set, b: set",
        "role_hierarchy": "child_level: int, parent_level: int",
        "permission_mask": "permissions: int, mask: int",
        "generate_token": "user_id: int, nonce: str",
        "validate_token": "token: str",
        "token_expiry": "issued_at: int, ttl_seconds: int",
        "refresh_token": "old_token: str",
        "create_session": "user_id: int",
        "revoke_session": "session_id: str, active: set",
        "session_ttl": "expires_at: int, now: int",
        "active_sessions": "sessions: list",
        "generate_otp": "seed: str",
        "verify_otp": "submitted: str, expected: str",
        "backup_codes": "codes: list, min_codes: int",
        "mfa_required": "risk_score: int, threshold: int",
        "clamp": "value: float, minimum: float, maximum: float",
        "normalize_email": "email: str",
        "slugify": "text: str",
        "safe_divide": "numerator: float, denominator: float, default: float = 0.0",
        "is_email": "value: str",
        "is_phone": "value: str",
        "is_uuid": "value: str",
        "is_positive": "value: float",
        "format_currency": "amount: float",
        "format_date": "year: int, month: int, day: int",
        "format_phone": "area: str, prefix: str, line: str",
        "truncate_text": "text: str, max_len: int",
        "to_snake_case": "name: str",
        "to_camel_case": "parts: list",
        "flatten_dict": "nested: list",
        "pick_keys": "data: dict, keys: list",
    }
    if op in sigs:
        return sigs[op]
    return "value: int, factor: float = 1.0"


def generate_src_module(domain: str, module: str, operations: list[str]) -> str:
    lines = [
        f'"""{domain.title()} {module} module — demo business logic."""',
        "",
    ]
    for op in operations:
        sig = op_signature(op)
        body = op_impl(op)
        if len(lines) > 2:
            lines.append("")
        lines.append(f"def {op}({sig}):")
        lines.append(f"    {body}")
    return "\n".join(lines).rstrip() + "\n"


def param_cases_for_op(op: str, count: int, domain: str, module: str) -> list[tuple[str, str]]:
    """Generate parametrize cases as (id, call_expr) pairs."""
    cases = []
    for i in range(count):
        seed = i + 1
        case_id = f"{domain}_{module}_{op}_{seed}"
        # Generic call based on operation patterns
        call = _generic_call(op, seed)
        cases.append((case_id, call))
    return cases


def _generic_call(op: str, seed: int) -> str:
    s = seed
    mapping = {
        "add_tax": f"add_tax({10 + s}, 0.0{s % 9 + 1})",
        "apply_discount": f"apply_discount({100 + s}, {s % 20})",
        "round_currency": f"round_currency({1.2345 * s}, 2)",
        "split_payment": f"split_payment({100 * s}, {2 + s % 5})",
        "generate_invoice_id": f"generate_invoice_id({1000 + s})",
        "format_line_item": f'format_line_item("SKU{s}", {s}, {9.99 + s})',
        "sum_line_items": f"sum_line_items([{{'amount': {s}}}, {{'amount': {s + 1}}}])",
        "validate_invoice": f"validate_invoice({s}, [{{'x': 1}}])",
        "apply_coupon": f"apply_coupon({50 + s}, 0.{s % 9 + 1})",
        "tier_discount": f"tier_discount({100 + s}, {s % 5})",
        "bulk_discount": f"bulk_discount({200 + s}, {s + 5})",
        "validate_promo": f'validate_promo("PROMO{s:04d}")',
        "calculate_refund": f"calculate_refund({100 + s}, {s % 50})",
        "partial_refund": f"partial_refund({100 + s}, 0.{s % 9 + 1})",
        "refund_eligible": f"refund_eligible({s}, 30)",
        "format_refund": f"format_refund({s})",
        "check_stock": f"check_stock({s + 10}, {s})",
        "reserve_stock": f"reserve_stock({s + 20}, {s})",
        "release_stock": f"release_stock({s}, {5})",
        "stock_level": f"stock_level({s}, 10)",
        "assign_bin": f'assign_bin("WH{s % 3}", {s}, {s % 20})',
        "locate_item": f'locate_item("SKU{s}")',
        "transfer_stock": f"transfer_stock({s + 5}, {s})",
        "warehouse_capacity": f"warehouse_capacity(1000, {s})",
        "reorder_point": f"reorder_point({float(s)}, 7, 5)",
        "suggest_quantity": f"suggest_quantity({s + 50}, {s})",
        "lead_time_days": f"lead_time_days(5, {s % 10})",
        "reorder_priority": f"reorder_priority({s * 10})",
        "count_variance": f"count_variance({s + 100}, {s + 98})",
        "adjust_count": f"adjust_count({s}, 2)",
        "schedule_count": f"schedule_count({s % 7})",
        "count_accuracy": f"count_accuracy(2.0, {s + 100})",
        "calculate_rate": f"calculate_rate(5.0, {float(s)}, 0.5)",
        "zone_rate": f"zone_rate(10.0, {1.0 + s * 0.1})",
        "weight_tier": f"weight_tier({s % 5}, 2.0, 5.0)",
        "express_surcharge": f"express_surcharge(10.0, {s % 2 == 0})",
        "track_status": f'track_status("{"shipped" if s % 2 else "pending"}")',
        "eta_estimate": f"eta_estimate({s % 5}, 2)",
        "format_tracking_id": f'format_tracking_id("abc{s}")',
        "delivery_window": "delivery_window(9, 17)",
        "generate_label": f"generate_label({s})",
        "validate_address": f'validate_address("123 St", "City", "{10000 + s}")',
        "package_dimensions": f"package_dimensions({float(s)}, 2.0, 3.0)",
        "label_format": f"label_format({s % 3 == 0})",
        "select_carrier": 'select_carrier(["fedex", "ups"])',
        "carrier_score": f"carrier_score(0.{80 + s % 20}, 0.{70 + s % 30})",
        "cutoff_time": f"cutoff_time({s % 24}, 18)",
        "service_level": f"service_level({s % 10})",
        "has_permission": 'has_permission("read", {"read", "write"})',
        "merge_roles": 'merge_roles({"admin"}, {"user", "read"})',
        "role_hierarchy": f"role_hierarchy({s % 5}, 3)",
        "permission_mask": "permission_mask(15, 7)",
        "generate_token": f'generate_token({s}, "n{s}")',
        "validate_token": f'validate_token("tok_{s}_abc12345")',
        "token_expiry": "token_expiry(1000, 3600)",
        "refresh_token": f'refresh_token("tok_user_{s}_abcdefgh")',
        "create_session": f"create_session({s})",
        "revoke_session": f'revoke_session("sess_{s}", {{"sess_{s + 1}"}})',
        "session_ttl": "session_ttl(5000, 1000)",
        "active_sessions": f"active_sessions([1, 2, None, {s}])",
        "generate_otp": f'generate_otp("seed{s}")',
        "verify_otp": 'verify_otp("123456", "123456")',
        "backup_codes": "backup_codes([1, 2, 3], 2)",
        "mfa_required": f"mfa_required({s * 10}, 50)",
        "clamp": f"clamp({float(s)}, 0.0, 10.0)",
        "normalize_email": f' normalize_email(" User{s}@Example.COM ")'.replace(" ", ""),
        "slugify": f'slugify("Hello World {s}")',
        "safe_divide": f"safe_divide({float(s)}, {1 if s % 5 else 0}, 0.0)",
        "is_email": f'is_email("user{s}@example.com")',
        "is_phone": f'is_phone("{5550000000 + s}")'[:30],
        "is_uuid": f'is_uuid("{"a" * 32}")',
        "is_positive": f"is_positive({float(s)})",
        "format_currency": f"format_currency({9.99 + s})",
        "format_date": f"format_date(2024, {1 + s % 12}, {1 + s % 28})",
        "format_phone": f'format_phone("555", "123", "{1000 + s}")',
        "truncate_text": f'truncate_text("long text number {s}", 10)',
        "to_snake_case": f'to_snake_case("MyVarName{s}")',
        "to_camel_case": f'to_camel_case(["hello", "world", "{s}"])',
        "flatten_dict": f"flatten_dict([{{'a': {s}}}, {{'b': {s + 1}}}])",
        "pick_keys": f"pick_keys({{'a': 1, 'b': 2, 'c': {s}}}, ['a', 'c'])",
    }
    if op in mapping:
        return mapping[op]
    return f"{op}({s}, {1.0 + s * 0.1})"


def generate_test_file(
    domain: str,
    module: str,
    operations: list[str],
    heavy: bool,
    slow: bool,
) -> str:
    func_count = HEAVY_FUNCTIONS if heavy else LIGHT_FUNCTIONS
    param_count = HEAVY_PARAM_COUNT if heavy else LIGHT_PARAM_COUNT
    ops = operations[:func_count]

    lines = [
        f'"""Tests for {domain}.{module} — generated; re-run scripts/generate_test_modules.py."""',
        "",
    ]
    if slow:
        lines.append("import time")
        lines.append("")
    lines.extend(
        [
            "import pytest",
            "",
            f"from src.{domain} import {module} as _module",
            "",
        ]
    )

    for idx, op in enumerate(ops):
        cases = param_cases_for_op(op, param_count, domain, module)
        ids = ", ".join(f'"{c[0]}"' for c in cases)
        params = ", ".join(repr(c[1]) for c in cases)

        if idx == 0 and slow:
            lines.append("@pytest.mark.slow")
        lines.append("@pytest.mark.parametrize(")
        lines.append('    "call_expr",')
        lines.append(f"    [{params}],")
        lines.append(f"    ids=[{ids}],")
        lines.append(")")
        lines.append(f"def test_{op}(call_expr):")
        lines.append('    """Execute operation and assert result is usable."""')
        if idx == 0 and slow:
            lines.append("    time.sleep(2 + (hash(call_expr) % 4))")
        lines.append("    result = eval(call_expr, vars(_module))")
        lines.append("    if isinstance(result, bool):")
        lines.append("        assert result in (True, False)")
        lines.append("    else:")
        lines.append("        assert result is not None")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def generate_package_init(domain: str) -> str:
    return f'"""{domain.title()} domain package."""\n'


def main() -> None:
    spec = load_spec()
    heavy_count = 0
    slow_domains_used = 0
    total_tests = 0
    file_count = 0

    for domain, domain_data in spec["domains"].items():
        write(ROOT / "src" / domain / "__init__.py", generate_package_init(domain))

        for mod in domain_data["modules"]:
            name = mod["name"]
            ops = mod["operations"]
            heavy = mod.get("heavy", False)
            if heavy:
                heavy_count += 1

            write(
                ROOT / "src" / domain / f"{name}.py",
                generate_src_module(domain, name, ops),
            )

            slow = slow_domains_used < 10 and heavy
            if slow:
                slow_domains_used += 1

            test_content = generate_test_file(domain, name, ops, heavy, slow)
            write(ROOT / "tests" / domain / f"test_{name}.py", test_content)

            func_count = HEAVY_FUNCTIONS if heavy else LIGHT_FUNCTIONS
            param_count = HEAVY_PARAM_COUNT if heavy else LIGHT_PARAM_COUNT
            total_tests += func_count * param_count
            file_count += 1

    print(f"Generated {file_count} test files (~{total_tests} parametrized tests)")
    print(f"Heavy modules: {heavy_count}")


if __name__ == "__main__":
    main()
