import unittest
from havok import Havok


class Test(unittest.TestCase):
    def test_it_decompiles_binary_files_to_a_havok_object(self):
        """ @test it decompiles binary files to a Havok object
        Given the file 12-16.hktmrb
        When the file path is passed to the Havok class
        Then the file should be decompiled into a Havok object
        """

        havok = Havok('../assets/12-16.hktmrb')

    def test_it_decompiles_the_file_header(self):
        """ @test it decompiles the file header
        Given the file 19-13.hknm2
        When the file path is passed to the Havok class
        Then the file header should be decompiled into the Havok object
        """

        havok = Havok('../assets/19-13.hknm2')
        self.assertEqual(havok.header.signature, b'W\xe0\xe0W\x10\xc0\xc0\x10')

    def test_it_decompiles_the_file_section_headers(self):
        """ @test it decompiles the file section headers
        Given the file Enemy_Assasin_Leader.hkrg
        When the file path is passed to the Havok class
        Then the file section headers should be decompiled into the Havok object
        """

        havok = Havok('../assets/Enemy_Assasin_Leader.hkrg')
        self.assertEqual(havok.section_header_tables.data.name, '__data__')
        self.assertEqual(havok.section_header_tables.data.start, 0x290)

    def test_it_decompiles_the_file_class_names(self):
        """ @test it decompiles the file class names
        Given the file FldObj_FallingRock_A_01.hkrb
        When the file path is passed to the Havok class
        Then the file class names list should be decompiled into the Havok object
        """

        havok = Havok('../assets/FldObj_FallingRock_A_01.hkrb')
        self.assertEqual(havok.classnames[5].name, 'hkpPhysicsData')
