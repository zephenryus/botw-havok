from typing import BinaryIO

from havok.SegmentHeaderOffsetTable import SegmentHeaderOffsetTable


class SegmentHeaderOffsetTables:
    def __init__(self, infile: BinaryIO) -> None:
        self.classnames = SegmentHeaderOffsetTable(infile)
        self.types = SegmentHeaderOffsetTable(infile)
        self.data = SegmentHeaderOffsetTable(infile)

    def __repr__(self):
        return "{} <classnames: {}, types: {}, data: {}>".format(
            self.__class__.__name__,
            self.classnames,
            self.types,
            self.data,
        )

    def __str__(self):
        return self.__repr__()
