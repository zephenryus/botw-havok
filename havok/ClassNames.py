import struct
from typing import BinaryIO

from havok.SegmentHeaderOffsetTable import SegmentHeaderOffsetTable
from havok.ClassName import ClassName


class ClassNames:
    class_names = []

    def __init__(self, infile: BinaryIO, offset_table: SegmentHeaderOffsetTable) -> None:
        classname_id = struct.unpack('>Ix', infile.read(5))[0]
        classname = b''

        classnames_buffer_size = offset_table.segment_abs_offset + offset_table.segment_rel_offsets[0]

        while infile.tell() < classnames_buffer_size:
            char = struct.unpack('>s', infile.read(1))[0]

            if char != b'\x00' and char != b'\xff':
                classname += char

            else:
                self.class_names.append(ClassName(
                    classname_id,
                    classname.decode('utf-8')
                ))

                if char == b'\xff' or infile.tell() + 5 > classnames_buffer_size:
                    break

                classname_id = struct.unpack('>Ix', infile.read(5))[0]
                classname = b''

    def __repr__(self):
        return "{} <class_names: [{}]>".format(self.__class__.__name__, ', '.join(map(repr, self.class_names)))

    def __str__(self):
        return self.__repr__()
