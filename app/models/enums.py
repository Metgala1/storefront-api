from enum import Enum


class UserRole(Enum):
    CUSTOMER = "CUSTOMER"
    ADMIN = "ADMIN"


class VideoStatus(Enum):
    PENDING = "PENDING"
    UPLOADED = "UPLOADED"
    FAILED = "FAILED"