import struct
from typing import BinaryIO

from .SectionHeader import SectionHeader
from .DataSectionOffsetTable import DataSectionOffsetTable
from .ClassNames import ClassNames

class Data(object):
    def __init__(self,
             infile: BinaryIO,
             data_section_header: SectionHeader,
             data_section_offset_table: DataSectionOffsetTable,
             classnames
             ) -> None:
        self.data = []
        self.data_section_offset_table = self._get_array_sizes(infile, data_section_offset_table, data_section_header.start)
        self._get_data(infile, data_section_header.start)

    def __getitem__(self, item):
        return self.data[item]

    def __repr__(self):
        return "{} <data: {}>".format(
            self.__class__.__name__,
            self.data
        )

    def _get_array_sizes(self, infile: BinaryIO,
                         data_section_offset_table: DataSectionOffsetTable,
                         section_start: int
                         ) -> DataSectionOffsetTable:
        for offset in data_section_offset_table:
            infile.seek(offset.meta + section_start)
            array_length, array_length_check = struct.unpack('>4x2I4x', infile.read(16))
            if array_length_check == array_length + 0x80000000:
                offset.array_length = array_length
            else:
                offset.array_length = 0

        return data_section_offset_table

    def _get_data(self, infile: BinaryIO, section_start: int):
        for offset in self.data_section_offset_table:
            infile.seek(offset.data + section_start)
            self.data.append(struct.unpack('>I', infile.read(4))[0])
