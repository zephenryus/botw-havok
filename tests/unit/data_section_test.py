import unittest
import havok


class TestDataSection(unittest.TestCase):
    def test_it_gets_the_array_lengths_for_each_data_segment(self):
        """ @test it gets the array lengths for each data segment
        Given the file FldObj_FallingRock_A_01.hkrb
        When the file is decompiled into data segments
        Then the array length of each segment should be on the object
        """

        with open('../assets/FldObj_FallingRock_A_01.hkrb', 'rb') as infile:
            infile.seek(0x40)
            classnames_header = havok.SectionHeader(infile)
            class_names = havok.ClassNames(infile, classnames_header)
            infile.seek(0xc0)
            data_header = havok.SectionHeader(infile)
            data_section_offset_table = havok.DataSectionOffsetTable(infile, 0x9d0, 80)
            data_section = havok.Data(infile, data_header, data_section_offset_table, class_names)

            self.assertEqual(data_section.data_section_offset_table[0].array_length, 1)
            self.assertEqual(data_section.data_section_offset_table[1].array_length, 0)
            self.assertEqual(data_section.data_section_offset_table[2].array_length, 0)
            self.assertEqual(data_section.data_section_offset_table[3].array_length, 1)
            self.assertEqual(data_section.data_section_offset_table[7].array_length, 7)
            self.assertEqual(data_section.data_section_offset_table[8].array_length, 50)

    def test_it_reads_the_first_byte_of_the_data(self):
        """ @test it reads the first byte of the data
        Given the file FldObj_FallingRock_A_01.hkrb
        When the file is decompiled into data segments
        Then the first byte of the data segment should be readable
        """

        with open('../assets/FldObj_FallingRock_A_01.hkrb', 'rb') as infile:
            infile.seek(0x40)
            classnames_header = havok.SectionHeader(infile)
            class_names = havok.ClassNames(infile, classnames_header)
            infile.seek(0xc0)
            data_header = havok.SectionHeader(infile)
            data_section_offset_table = havok.DataSectionOffsetTable(infile, 0x9d0, 80)
            data_section = havok.Data(infile, data_header, data_section_offset_table, class_names)

            self.assertEqual(data_section[0], 0x00000000)
            self.assertEqual(data_section[1], 0x50687973)
            self.assertEqual(data_section[2], 0x686b7050)
            self.assertEqual(data_section[3], 0x00000000)
            self.assertEqual(data_section[7], 0x3fb16393)
