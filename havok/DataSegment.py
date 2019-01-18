from havok.SegmentHeaderOffsetTable import SegmentHeaderOffsetTable
from havok.DataSegmentOffsetTable import DataSegmentOffsetTable


class DataSegment:
    def __init__(self, infile, offset_table: SegmentHeaderOffsetTable) -> None:
        self.start_offset = offset_table.abs_offset
        self.end_offset = offset_table.rel_offsets[5]
        self.size = self.end_offset.abs_offset - self.start_offset
        self.data_offset_table = DataSegmentOffsetTable(
            infile,
            offset_table.rel_offsets[0].abs_offset,
            offset_table.rel_offsets[0].size
        )
        self.length = len(self.data_offset_table)

    def __repr__(self):
        return "{} <segment_start: {}, segment_end: {}, size: {}, length: {}, offset_table: [{}]>".format(
            self.__class__.__name__,
            hex(self.start_offset),
            hex(self.end_offset.abs_offset),
            self.size,
            self.length,
            self.data_offset_table
        )
