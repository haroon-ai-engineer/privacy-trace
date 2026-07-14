from enum import Enum


class PIIType(str, Enum):
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    CREDIT_CARD = "CREDIT_CARD"
    API_KEY = "API_KEY"
    JWT = "JWT"
    IP_ADDRESS = "IP_ADDRESS"
    CNIC = "CNIC"


class Severity(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"