from enum import Enum


class MessageType(Enum):
    PRODUCT = 'PRODUCT'
    CATEGORY = 'CATEGORY'
    BRAND = 'BRAND'
    SUPPLIER = 'SUPPLIER'
    INVENTORY = 'INVENTORY'
    SALE = 'SALE'
    GREETING = 'GREETING'
    UNKNOWN = 'UNKNOWN'
