import unittest
import havok
from havok import Havok


def init_data():
    havok = Havok('../assets/FldObj_FallingRock_A_01.hkrb')
    return havok.section_header_tables.data


class TestDataSectionOffsetTable(unittest.TestCase):
    data_section_header_table = init_data()

    def test_is_can_decompile_the_data_offset_table(self):
        """ @test is can decompile the data offset table
        Given the file FldObj_FallingRock_A_01.hkrb
        When the file is passed to the DataSectionOffsetTable class
        Then the list of offsets should be decompiled
        """

        with open('../assets/FldObj_FallingRock_A_01.hkrb', 'rb') as infile:
            data_section_offset_table = havok.DataSectionOffsetTable(
                infile,
                self.data_section_header_table.offsets[0].abs_offset,
                self.data_section_header_table.offsets[0].size
            )
            self.assertEqual(data_section_offset_table[0].meta, 0)
            self.assertEqual(data_section_offset_table[0].data, 16)
            self.assertEqual(data_section_offset_table[4].meta, 120)
            self.assertEqual(data_section_offset_table[4].data, 192)
