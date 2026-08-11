"""Auth permissions module — demo business logic."""

def has_permission(permission: str, role_permissions: set):
    return permission in role_permissions

def merge_roles(a: set, b: set):
    return sorted(set(a) | set(b))

def role_hierarchy(child_level: int, parent_level: int):
    return child_level <= parent_level + 1

def permission_mask(permissions: int, mask: int):
    return permissions & mask
