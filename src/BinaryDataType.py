from enum import Enum, auto, unique

@unique
class BinaryDataType(Enum):
    Int32 = auto()
    Int64 = auto()
    UInt32 = auto()
    UInt64 = auto()
    Single = auto()
    Double = auto()