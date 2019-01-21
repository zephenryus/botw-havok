import unittest

import havok


class TestSectionHeaders(unittest.TestCase):
    def test_it_can_decompile_the_classname_section_header(self):
        """ @test it can decompile the classname section header
        Given the file G-6-2.hksc
        When the file is passed to the SectionHeader class
        Then the section header should be __classnames__ at offset 0x100
        """

        with open('../assets/G-6-2.hksc', 'rb') as infile:
            infile.seek(64)
            section_header = havok.SectionHeader(infile)
            self.assertEqual(section_header.name, '__classnames__')
            self.assertEqual(section_header.start, 0x100)

    def test_it_can_decompile_all_three_section_headers(self):
        """ @test it can decompile all three section headers
        Given the file Enemy_Assasin_Leader.hkrg
        When the file is passed to the SectionHeader class
        Then the section headers for __classnames__, __types__ and __data__ should be decompiled
        """

        with open('../assets/Enemy_Assasin_Leader.hkrg', 'rb') as infile:
            infile.seek(64)
            section_header_classnames = havok.SectionHeader(infile)
            section_header_types = havok.SectionHeader(infile)
            section_header_data = havok.SectionHeader(infile)

            self.assertEqual(section_header_classnames.name, '__classnames__')
            self.assertEqual(section_header_classnames.start, 0x100)
            self.assertEqual(section_header_types.name, '__types__')
            self.assertEqual(section_header_types.start, 0x290)
            self.assertEqual(section_header_data.name, '__data__')
            self.assertEqual(section_header_data.start, 0x290)

    def test_the_section_header_tables_decompiles_all_section_headers(self):
        """ @test the SectionHeaderTables decompiles all section headers
        Given the file 19-13.hknm2
        When the file is passed to the SectionHeaderTables class
        Then all three section headers are decompiled into the container
        """

        with open('../assets/19-13.hknm2', 'rb') as infile:
            infile.seek(80)
            section_header_tables = havok.SectionHeaderTables(infile)
            self.assertEqual(section_header_tables.classnames.name, '__classnames__')
            self.assertEqual(section_header_tables.types.name, '__types__')
            self.assertEqual(section_header_tables.data.name, '__data__')
