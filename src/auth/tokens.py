"""Auth tokens module — demo business logic."""


def generate_token(user_id: int, nonce: str):
    return f"tok_{user_id}_{nonce}"


def validate_token(token: str):
    return token.startswith("tok_") and len(token) > 8


def token_expiry(issued_at: int, ttl_seconds: int):
    return issued_at + ttl_seconds


def refresh_token(old_token: str):
    return f"ref_{old_token[-8:]}"
