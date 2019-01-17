import struct
from typing import BinaryIO


class SegmentHeaderOffsetTable:
    def __init__(self, infile: BinaryIO) -> None:
        """
        Decompiles Havok Segment Header Offset Table Binary into a Python object

        :param infile (BinaryIO): Source file to decompile segment header offset table data from
        """

        self.table_name = struct.unpack('>19sx', infile.read(20))[0].decode('utf-8').strip(' \0')
        self.segment_rel_offsets = [0, 0, 0, 0, 0, 0]
        self.segment_abs_offset, \
            self.segment_rel_offsets[0], \
            self.segment_rel_offsets[1], \
            self.segment_rel_offsets[2], \
            self.segment_rel_offsets[3], \
            self.segment_rel_offsets[4], \
            self.segment_rel_offsets[5] = struct.unpack('>7I16x', infile.read(44))

    def __repr__(self) -> str:
        """
        Generates a string representation of the SegmentHeaderOffsetTable class

        :return: string representation of SegmentHeaderOffsetTable class
        :rtype:  str
        """

        return "{} <table_name: '{}', segment_abs_offset: {}, segment_rel_offsets: [{}]>".format(
            self.__class__.__name__,
            self.table_name,
            hex(self.segment_abs_offset),
            ', '.join(map(hex, self.segment_rel_offsets))
        )

    def __str__(self):
        """
        Generates a string representation of the SegmentHeaderOffsetTable class

        __str__ is an alias for __repr__

        :return: string representation of SegmentHeaderOffsetTable class
        :rtype:  str
        """

        return self.__repr__()
