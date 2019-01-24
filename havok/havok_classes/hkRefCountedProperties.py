from enum import Enum
from .hkRefCountedPropertiesEntry import hkRefCountedPropertiesEntry


class ReferenceCountHandling(Enum):
    REFERENCE_COUNT_INCREMENT = 0
    REFERENCE_COUNT_IGNORE = 1


class hkRefCountedProperties(object):
    entries: hkRefCountedPropertiesEntry