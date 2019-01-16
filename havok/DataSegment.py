import struct

from havok.DataSegmentOffsetTable import DataSegmentOffsetTable
from havok.DataSegmentOffsetTableItem import DataSegmentOffsetTableItem


class DataSegment:
    def __init__(self, infile, abs_offs: int, rel_offs_table: list):
        self.segment_start = abs_offs
        self.segment_end = 0
        self.offset_table = self.normalize_offset_table(rel_offs_table)

        offset_table_length = len(self.offset_table)
        # self.unknown_table = self.get_data_offset_table(
        #     infile,
        #     self.offset_table[offset_table_length - 1],
        #     self.segment_end,
        #     self.segment_start
        # )
        self.data_offset_table = self.get_data_offset_table(
            infile,
            self.offset_table[offset_table_length - 2],
            self.offset_table[offset_table_length - 1],
            self.segment_start
        )
        print(self.data_offset_table)

    def normalize_offset_table(self, rel_offs_table: list) -> list:
        offsets = [self.segment_start]
        last_offset = 0

        for offset in rel_offs_table:
            if last_offset != offset:
                offsets.append(offset + self.segment_start)
            last_offset = offset

        self.segment_end = last_offset + self.segment_start

        del offsets[-1]

        return offsets

    def get_data_offset_table(self, infile, segment_offset, segment_end, segment_start):
        infile.seek(segment_offset)

        offset_table = DataSegmentOffsetTable()
        while infile.tell() < segment_end:
            meta_offset, data_offset = struct.unpack('>2i', infile.read(8))

            if meta_offset != -1 and data_offset != -1:
                offset_table.append(DataSegmentOffsetTableItem(
                    meta_offset + segment_start,
                    data_offset + segment_start
                ))

        return offset_table

    def __repr__(self):
        return "{} <segment_start: {}, segment_end: {}, offset_table: [{}]>".format(
            self.__class__.__name__,
            hex(self.segment_start),
            hex(self.segment_end),
            ', '.join(map(hex, self.offset_table))
        )

