import struct


class SegmentHeaderOffsetTable:
    def __init__(self, data: bytes):
        self.table_name = struct.unpack('>19sx', data[0:20])[0].decode('utf-8').strip(' \0')
        self.segment_rel_offsets = [0, 0, 0, 0, 0, 0]
        self.segment_abs_offset, \
            self.segment_rel_offsets[0], \
            self.segment_rel_offsets[1], \
            self.segment_rel_offsets[2], \
            self.segment_rel_offsets[3], \
            self.segment_rel_offsets[4], \
            self.segment_rel_offsets[5] = struct.unpack('>7I16x', data[20:64])

    def __repr__(self):
        return "{} <table_name: '{}', segment_abs_offset: {}, segment_rel_offsets: [{}]>".format(
            self.__class__.__name__,
            self.table_name,
            hex(self.segment_abs_offset),
            ', '.join(map(hex, self.segment_rel_offsets))
        )

    def __str__(self):
        return self.__repr__()
