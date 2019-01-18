import struct
from typing import List, BinaryIO

from havok.DataSegmentOffsetTableItem import DataSegmentOffsetTableItem


class DataSegmentOffsetTable:
    items: List[DataSegmentOffsetTableItem]
    next_index = 0

    def __init__(self, infile: BinaryIO, table_start: int, table_length: int) -> None:
        self.items = []
        infile.seek(table_start)
        last_offset = 0

        while infile.tell() + 8 < table_start + table_length:
            meta_offset, data_offset = struct.unpack('>2i', infile.read(8))

            if meta_offset != -1 and data_offset != -1:
                self.append(DataSegmentOffsetTableItem(
                    meta_offset,
                    data_offset,
                    data_offset - last_offset
                ))
                last_offset = data_offset

    def append(self, data: DataSegmentOffsetTableItem):
        self.items.append(data)

    def __iter__(self):
        return self.items

    def __next__(self):
        if self.next_index > len(self.items):
            raise StopIteration
        else:
            item = self.items[self.next_index]
            self.next_index += 1
            return item

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return "{} <items: {}>".format(
            self.__class__.__name__,
            ', '.join(map(repr, self.items))
        )
