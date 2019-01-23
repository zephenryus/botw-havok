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
    data: Data

    MULTI_FILE_CLASSNAMES = [
        "StaticCompoundInfo"
    ]

    def __init__(self, path: str, file_start=0) -> None:
        with open(path, 'rb') as infile:
            infile.seek(file_start)
            self.header = Header(infile)
            self.section_header_tables = SectionHeaderTables(infile, file_start)
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
                self.classnames,
                file_start
            )

    def __repr__(self) -> str:
        return "{} <header: {}, section_header_tables: {}, classnames: {}, data_section_offset_table: {}, data: {}>".format(
            self.__class__.__name__,
            self.header,
            self.section_header_tables,
            self.classnames,
            self.data_section_offset_table,
            self.data
        )

    def is_multi_file(self) -> bool:
        for classname in self.classnames:
            if classname.name in self.MULTI_FILE_CLASSNAMES:
                return True

        return False
