import struct


class Header:
    def __init__(self, data: bytes):
        self.signature = struct.unpack('>8s', data[0:8])[0]
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
            self.unk10 = struct.unpack('>2I4B5I', data[8:40])
        self.version = struct.unpack('>14s2x', data[40:56])[0].decode('utf-8')
        self.unk11, \
            self.unk12, \
            self.unk13, \
            self.unk14, \
            self.unk15, \
            self.unk16, \
            self.unk17, \
            self.unk18 = struct.unpack('>I4H3I', data[56:80])
