import struct
from typing import List

from havok import Havok


class ActorInfo(object):
    HashId: int
    SRTHash: int
    ShapeInfoStart: int
    ShapeInfoEnd: int

    def __init__(self, data: tuple) -> None:
        self.HashId = data[0]
        self.SRTHash = data[1]
        self.ShapeInfoStart = data[2]
        self.ShapeInfoEnd = data[3]


class ShapeInfo(object):
    ActorInfoIndex: int
    InstanceId: int
    BodyGroup: int
    BodyLayerType: int

    def __init__(self, data: tuple) -> None:
        self.ActorInfoIndex = data[0]
        self.InstanceId = data[1]
        self.BodyGroup = data[2]
        self.BodyLayerType = data[3]


class StaticCompoundInfo(object):
    Offset: int
    ActorInfo: List[ActorInfo]
    ShapeInfo: List

    def __init__(self):
        self.Offset = 0
        self.ActorInfo = []
        self.ShapeInfo = []


def main():
    path = '../assets/G-6-2.hksc'
    havok = Havok(path)
    print(havok.section_header_tables.data)
    print(havok.data_section_offset_table)

    static_compound_info = StaticCompoundInfo()

    with open(path, 'rb') as infile:
        infile.seek(havok.section_header_tables.data.start)
        static_compound_info.Offset = struct.unpack('>I', infile.read(4))[0]

        infile.seek(havok.section_header_tables.data.start + havok.data_section_offset_table[0].data)

        for _ in range(havok.data_section_offset_table[0].array_length):
            data = struct.unpack('>4I', infile.read(16))
            print(data)
            static_compound_info.ActorInfo.append(ActorInfo(
                data
            ))

        infile.seek(havok.section_header_tables.data.start + havok.data_section_offset_table[1].data)

        for _ in range(havok.data_section_offset_table[1].array_length):
            data = struct.unpack('>2i2b2x', infile.read(12))
            print(data)
            static_compound_info.ShapeInfo.append(ShapeInfo(
                data
            ))

        print(static_compound_info.ActorInfo)
        print(static_compound_info.ShapeInfo)


if __name__ == "__main__":
    main()
