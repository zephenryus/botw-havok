import struct
from typing import BinaryIO, List

from .SectionHeaderItem import SectionHeaderItem


class SectionHeader(object):
    name: str
    start: int
    offsets: List[SectionHeaderItem]

    def __init__(self, infile: BinaryIO, file_start=0) -> None:
        """
        Decompiles Havok Segment Header Offset Table Binary into a Python object

        :param infile (BinaryIO): Source file to decompile segment header offset table data from
        """

        self.name = struct.unpack('>19sx', infile.read(20))[0].decode('utf-8').strip(' \0')
        # Relative offsets
        rel_offs = [0, 0, 0, 0, 0, 0]
        self.start, \
            rel_offs[0], \
            rel_offs[1], \
            rel_offs[2], \
            rel_offs[3], \
            rel_offs[4], \
            rel_offs[5] = struct.unpack('>7I16x', infile.read(44))

        self.start += file_start
        self.offsets = [
            SectionHeaderItem(rel_offs[0], self.start + rel_offs[0], rel_offs[1] - rel_offs[0]),
            SectionHeaderItem(rel_offs[1], self.start + rel_offs[1], rel_offs[2] - rel_offs[1]),
            SectionHeaderItem(rel_offs[2], self.start + rel_offs[2], rel_offs[3] - rel_offs[2]),
            SectionHeaderItem(rel_offs[3], self.start + rel_offs[3], rel_offs[4] - rel_offs[3]),
            SectionHeaderItem(rel_offs[4], self.start + rel_offs[4], rel_offs[5] - rel_offs[4]),
            SectionHeaderItem(rel_offs[5], self.start + rel_offs[5], 0)
        ]

    def __repr__(self) -> str:
        """
        Generates a string representation of the SegmentHeaderOffsetTable class

        :return: string representation of SegmentHeaderOffsetTable class
        :rtype:  str
        """

        return "{} <name: '{}', start: {}, offsets: [{}]>".format(
            self.__class__.__name__,
            self.name,
            hex(self.start),
            self.offsets
        )

    def __str__(self):
        """
        Generates a string representation of the SegmentHeaderOffsetTable class

        __str__ is an alias for __repr__

        :return: string representation of SegmentHeaderOffsetTable class
        :rtype:  str
        """

        return self.__repr__()
