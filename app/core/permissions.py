from enum import Enum


class UserRole(str, Enum):
    CUSTOMER = "CUSTOMER"
    ADMIN = "ADMIN"


class Permission(str, Enum):
    PRODUCTS_READ = "products:read"
    PRODUCTS_CREATE = "products:create"
    PRODUCTS_UPDATE = "products:update"
    PRODUCTS_DELETE = "products:delete"
    USERS_READ = "users:read"
    USERS_MANAGE = "users:manage"


ROLE_PERMISSIONS = {
    UserRole.ADMIN: {
        Permission.PRODUCTS_READ,
        Permission.PRODUCTS_CREATE,
        Permission.PRODUCTS_UPDATE,
        Permission.PRODUCTS_DELETE,
        Permission.USERS_READ,
        Permission.USERS_MANAGE,
    },

    UserRole.CUSTOMER: {
        Permission.PRODUCTS_READ,
    },
}