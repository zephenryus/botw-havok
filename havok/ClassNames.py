import struct

from havok.ClassName import ClassName


class ClassNames:
    class_names = []

    def read_bytes(self, data: bytes):
        pos = 0
        classname_id = struct.unpack('>Ix', data[pos:pos + 5])[0]
        classname = b''
        pos += 5

        while pos < len(data):
            char = struct.unpack('>s', data[pos:pos + 1])[0]
            pos += 1

            if char != b'\x00' and char != b'\xff':
                classname += char

            else:
                self.class_names.append(ClassName(
                    classname_id,
                    classname.decode('utf-8')
                ))

                if char == b'\xff' or pos + 5 > len(data):
                    break

                classname_id = struct.unpack('>Ix', data[pos:pos + 5])[0]
                classname = b''
                pos += 5

        return self

    def __repr__(self):
        return "{} <class_names: [{}]>".format(self.__class__.__name__, ', '.join(map(repr, self.class_names)))

    def __str__(self):
        return self.__repr__()
