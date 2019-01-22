from typing import List

from .Header import Header
from .SectionHeaderTables import SectionHeaderTables
from .ClassNames import ClassNames
from .ClassName import ClassName
from .DataSectionOffsetTable import DataSectionOffsetTable
from .Data import Data


class Havok(object):
    header: Header
    section_header_tables: SectionHeaderTables
    classnames: List[ClassName]
    data_section_offset_table: DataSectionOffsetTable

    def __init__(self, path: str) -> None:
        with open(path, 'rb') as infile:
            self.header = Header(infile)
            self.section_header_tables = SectionHeaderTables(infile)
            self.classnames = ClassNames(infile, self.section_header_tables.classnames)
            self.data_section_offset_table = DataSectionOffsetTable(
                infile,
                self.section_header_tables.data.offsets[0].abs_offset,
                self.section_header_tables.data.offsets[0].size
            )
            self.data = Data(
                infile,
                self.section_header_tables.data,
                self.data_section_offset_table,
                self.classnames
            )

    def __repr__(self):
        return "{} <header: {}, section_header_tables: {}, classnames: {}>".format(
            self.__class__.__name__,
            self.header,
            self.section_header_tables,
            self.classnames
        )
