import struct
from typing import BinaryIO


class Header(object):
    signature: bytes
    version: str
    size: int
    unk00: int
    unk01: int
    unk02: int
    unk03: int
    unk04: int
    unk05: int
    unk06: int
    unk07: int
    unk08: int
    unk09: int
    unk10: int
    unk11: int
    unk12: int
    unk13: int
    unk14: int
    unk15: int
    unk16: int
    unk17: int
    unk18: int

    def __init__(self, infile: BinaryIO) -> None:
        """
        Decompiles Havok Header Binary into a Python object

        :param infile (BinaryIO): Source file to decompile header data from
        """

        self.signature, self.unk00, self.unk01, self.unk02, self.unk03, self.unk04, self.unk05, self.unk06, self.unk07, \
            self.unk08, self.unk09, self.unk10, version, self.unk11, self.unk12, self.unk13 = struct.unpack(
                '>8s2I4B5I14s2xI2H', infile.read(64))

        self.version = version.decode('utf-8')
        self.size = 64

        if self.is_long():
            self.unk14, self.unk15, self.unk16, self.unk17, self.unk18 = struct.unpack('>2H3I', infile.read(16))

            self.size = 80

    def is_long(self) -> bool:
        """
        Checks if header is short (64 bytes) or long (80 bytes)

        :return: True if long, otherwise False
        :rtype:  bool
        """

        return self.unk13 == 16

    def __repr__(self) -> str:
        """
        Generates a string representation of the Header class

        :return: string representation of Header class
        :rtype:  str
        """

        return_string = "{} <signature: 0x{}, size: {}, unk00: {}, unk01: {}, unk02: {}, unk03: {}, unk04: {}, unk05: {}, unk06: {}, unk07: {}, unk08: {}, unk09: {}, unk10: {}, version: '{}', unk11: {}, unk12: {}, unk13: {}>".format(
            self.__class__.__name__,
            self.signature.hex(),
            self.size,
            self.unk00,
            self.unk01,
            self.unk02,
            self.unk03,
            self.unk04,
            self.unk05,
            self.unk06,
            self.unk07,
            self.unk08,
            self.unk09,
            self.unk10,
            self.version,
            self.unk11,
            self.unk12,
            self.unk13
        )

        if self.is_long():
            return_string = return_string[:-1]
            return_string += ", unk14: {}, unk15: {}, unk16: {}, unk17: {}, unk18: {}>".format(
                self.unk14,
                self.unk15,
                self.unk16,
                self.unk17,
                self.unk18,
            )

        return return_string

    def __str__(self) -> str:
        """
        Generates a string representation of the Header class

        __str__ is an alias for __repr__

        :return: string representation of Header class
        :rtype:  str
        """
        return self.__repr__()
