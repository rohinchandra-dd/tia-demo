"""Auth sessions module — demo business logic."""


def create_session(user_id: int):
    return f"sess_{user_id}"


def revoke_session(session_id: str, active: set):
    return session_id not in active


def session_ttl(expires_at: int, now: int):
    return max(0, expires_at - now)


def active_sessions(sessions: list):
    return len([s for s in sessions if s])
