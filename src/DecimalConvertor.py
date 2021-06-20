
from BinaryDataType import BinaryDataType
import struct
import binascii

def getSize(dataType: BinaryDataType) -> int:
  SIZES = {
    BinaryDataType.Single: 4,
    BinaryDataType.Double: 8,
    BinaryDataType.Int32: 4,
    BinaryDataType.Int64: 8,
    BinaryDataType.UInt32: 4,
    BinaryDataType.UInt64: 8,
  }
  return SIZES[dataType] * 2

def getDataIndicator(dataType: BinaryDataType) -> str:
  INDICATORS = {
    BinaryDataType.Single: "f",
    BinaryDataType.Double: "d",
    BinaryDataType.Int32: "i",
    BinaryDataType.Int64: "q",
    BinaryDataType.UInt32: "I",
    BinaryDataType.UInt64: "Q",
  }
  return INDICATORS[dataType]

def convertToDecimal(input: str, dataType: BinaryDataType) -> str:
  size = getSize(dataType)
  indicator = getDataIndicator(dataType)
  textWOSpaces = input.replace(" ", "")
  hexNumbers = [(textWOSpaces[i:i+size].rjust(size, "0")) for i in range(0, len(textWOSpaces), size)]
  unpackedData = [struct.unpack(indicator, binascii.unhexlify(hexStr))[0] for hexStr in hexNumbers]
  return " ".join([str(number) for number in unpackedData])