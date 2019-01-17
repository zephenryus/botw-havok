import struct


class Header:
    def __init__(self, infile):
        self.signature, \
        self.unk00, \
        self.unk01, \
        self.unk02, \
        self.unk03, \
        self.unk04, \
        self.unk05, \
        self.unk06, \
        self.unk07, \
        self.unk08, \
        self.unk09, \
        self.unk10, \
        self.version, \
        self.unk11, \
        self.unk12, \
        self.unk13 = struct.unpack('>8s2I4B5I14s2xI2H', infile.read(64))

        self.size = 64

        if self.is_long():
            self.unk14, \
            self.unk15, \
            self.unk16, \
            self.unk17, \
            self.unk18 = struct.unpack('>2H3I', infile.read(16))

            self.size = 80

    def is_long(self) -> bool:
        return self.unk13 == 16

    def __repr__(self):
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
            self.version.decode('utf-8'),
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
