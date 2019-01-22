import struct
from typing import BinaryIO, List

from .DataSectionOffsetTableItem import DataSectionOffsetTableItem


class DataSectionOffsetTable(object):
    items: List[DataSectionOffsetTableItem]
    _next_index: int

    def __init__(self, infile: BinaryIO, table_start: int, table_size: int) -> None:
        self.items = []
        infile.seek(table_start)
        last_offset = 0
        self._next_index = 0

        while infile.tell() + 8 < table_start + table_size:
            meta_offset, data_offset = struct.unpack('>2i', infile.read(8))

            if meta_offset != -1 and data_offset != -1:
                self.append(DataSectionOffsetTableItem(
                    meta_offset,
                    data_offset,
                    data_offset - last_offset
                ))
                last_offset = data_offset

    def append(self, data: DataSectionOffsetTableItem) -> int:
        self.items.append(data)
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __next__(self):
        if self._next_index > len(self.items):
            raise StopIteration
        else:
            item = self.items[self._next_index]
            self._next_index += 1
            return item

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def __repr__(self):
        return "{} <items: {}>".format(
            self.__class__.__name__,
            ', '.join(map(repr, self.items))
        )
