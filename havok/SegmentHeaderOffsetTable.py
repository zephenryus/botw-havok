import struct
from typing import BinaryIO, List

from havok.SegmentHeaderOffsetTableItem import SegmentHeaderOffsetTableItem


class SegmentHeaderOffsetTable:
    table_name: str
    abs_offset: int
    rel_offsets: List[SegmentHeaderOffsetTableItem]

    def __init__(self, infile: BinaryIO) -> None:
        """
        Decompiles Havok Segment Header Offset Table Binary into a Python object

        :param infile (BinaryIO): Source file to decompile segment header offset table data from
        """

        self.table_name = struct.unpack('>19sx', infile.read(20))[0].decode('utf-8').strip(' \0')
        rel_offsets = [0, 0, 0, 0, 0, 0]
        self.abs_offset, \
            rel_offsets[0], \
            rel_offsets[1], \
            rel_offsets[2], \
            rel_offsets[3], \
            rel_offsets[4], \
            rel_offsets[5] = struct.unpack('>7I16x', infile.read(44))

        self.rel_offsets = [
            SegmentHeaderOffsetTableItem(rel_offsets[0], self.abs_offset + rel_offsets[0], rel_offsets[1] - rel_offsets[0]),
            SegmentHeaderOffsetTableItem(rel_offsets[1], self.abs_offset + rel_offsets[1], rel_offsets[2] - rel_offsets[1]),
            SegmentHeaderOffsetTableItem(rel_offsets[2], self.abs_offset + rel_offsets[2], rel_offsets[3] - rel_offsets[2]),
            SegmentHeaderOffsetTableItem(rel_offsets[3], self.abs_offset + rel_offsets[3], rel_offsets[4] - rel_offsets[3]),
            SegmentHeaderOffsetTableItem(rel_offsets[4], self.abs_offset + rel_offsets[4], rel_offsets[5] - rel_offsets[4]),
            SegmentHeaderOffsetTableItem(rel_offsets[5], self.abs_offset + rel_offsets[5], 0)
        ]

    def __repr__(self) -> str:
        """
        Generates a string representation of the SegmentHeaderOffsetTable class

        :return: string representation of SegmentHeaderOffsetTable class
        :rtype:  str
        """

        return "{} <table_name: '{}', abs_offset: {}, rel_offsets: [{}]>".format(
            self.__class__.__name__,
            self.table_name,
            hex(self.abs_offset),
            self.rel_offsets
        )

    def __str__(self):
        """
        Generates a string representation of the SegmentHeaderOffsetTable class

        __str__ is an alias for __repr__

        :return: string representation of SegmentHeaderOffsetTable class
        :rtype:  str
        """

        return self.__repr__()
