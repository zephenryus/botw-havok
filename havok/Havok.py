from .DataSegment import DataSegment
from .ClassNames import ClassNames
from .Header import Header
from .SegmentHeaderOffsetTables import SegmentHeaderOffsetTables


class Havok:
    header: Header
    segment_header_offset_tables: SegmentHeaderOffsetTables

    def __init__(self, path: str) -> None:
        with open(path, 'rb') as infile:
            self.header = Header(infile)
            self.segment_header_offset_tables = SegmentHeaderOffsetTables(infile)
            self.classnames = ClassNames(infile, self.segment_header_offset_tables.classnames)
            self.data_segment = DataSegment(infile, self.segment_header_offset_tables.data)
            self.data = Data(infile, self.data_segment, self.classnames)

    def __repr__(self):
        return "{} <header: {}, segment_header_offset_tables: {}, classnames: {}>".format(
            self.__class__.__name__,
            self.header,
            self.segment_header_offset_tables,
            self.classnames
        )
