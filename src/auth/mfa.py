"""Auth mfa module — demo business logic."""


def generate_otp(seed: str):
    return str(abs(hash(seed)) % 1000000).zfill(6)


def verify_otp(submitted: str, expected: str):
    return submitted == expected


def backup_codes(codes: list, min_codes: int):
    return len(codes) >= min_codes


def mfa_required(risk_score: int, threshold: int):
    return risk_score >= threshold
