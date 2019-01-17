from havok.SegmentHeaderOffsetTable import SegmentHeaderOffsetTable
from havok.Header import Header


def main():
    files = [
        'assets/12-16.hktmrb',
        'assets/19-13.hknm2',
        'assets/Enemy_Assasin_Leader.hkrg',
        'assets/FldObj_FallingRock_A_01.hkrb',
        'assets/G-6-2.hksc',
        'assets/Npc_King_Vagrant.hkcl'
    ]

    for filename in files:
        with open(filename, 'rb') as infile:
            Header(infile)  # Seek past the header
            for _ in range(3):
                segment_header_offset_table = SegmentHeaderOffsetTable(infile)
                print(segment_header_offset_table)


if __name__ == "__main__":
    main()
