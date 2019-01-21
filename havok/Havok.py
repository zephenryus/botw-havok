from typing import List

from .Header import Header
from .SectionHeaderTables import SectionHeaderTables
from .ClassNames import ClassNames
from .ClassName import ClassName


class Havok(object):
    header: Header
    section_header_tables: SectionHeaderTables
    classnames: List[ClassName]

    def __init__(self, path: str) -> None:
        with open(path, 'rb') as infile:
            self.header = Header(infile)
            self.section_header_tables = SectionHeaderTables(infile)
            self.classnames = ClassNames(infile, self.section_header_tables.classnames)
            # self.data_segment = DataSegment(infile, self.section_header_tables.data)
            # self.data = Data(infile, self.data_segment, self.classnames)

    def __repr__(self):
        return "{} <header: {}, segment_header_offset_tables: {}, classnames: {}>".format(
            self.__class__.__name__,
            self.header,
            self.section_header_tables,
            self.classnames
        )
