import struct
from typing import BinaryIO, List

from havok.SectionHeader import SectionHeader
from havok.ClassName import ClassName


class ClassNames(object):
    class_names: List

    def __init__(self, infile: BinaryIO, section_header: SectionHeader) -> None:
        assert section_header.name == '__classnames__'
        self.class_names = []

        classnames_buffer_end = section_header.offsets[0].abs_offset
        classname_id = struct.unpack('>Ix', infile.read(5))[0]
        classname = b''

        while infile.tell() < classnames_buffer_end:
            char = struct.unpack('>s', infile.read(1))[0]

            if char != b'\x00' and char != b'\xff':
                classname += char

            else:
                self.class_names.append(ClassName(
                    classname_id,
                    classname.decode('utf-8')
                ))

                if char == b'\xff' or infile.tell() + 5 > classnames_buffer_end:
                    break

                classname_id = struct.unpack('>Ix', infile.read(5))[0]
                classname = b''

    def __len__(self):
        return len(self.class_names)

    def __getitem__(self, item):
        return self.class_names[item]

    def __repr__(self):
        return "{} <class_names: [{}]>".format(self.__class__.__name__, ', '.join(map(repr, self.class_names)))

    def __str__(self):
        return self.__repr__()
