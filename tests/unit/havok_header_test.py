import unittest

import havok


class TestHavokHeader(unittest.TestCase):
    def test_it_can_decompile_a_header(self):
        """ @test it can decompile a header
        Given the file G-6-2.hksc
        When the file is passed to the Havok Header class
        Then the header should contain the file signature, correct header size and Havok version string
        """

        with open('../assets/G-6-2.hksc', 'rb') as infile:
            header = havok.Header(infile)
            print(header.version)
            self.assertEqual(header.signature, b'W\xe0\xe0W\x10\xc0\xc0\x10')
            self.assertEqual(header.size, 64)
            self.assertEqual(header.version, 'hk_2014.2.0-r1')

    def test_it_can_decompile_a_long_header(self):
        """ @test it can decompile a long header
        Given the file 19-13.hknm2
        When the file is passed to the Header class
        Then the header size should be 80 bytes
        """

        with open('../assets/19-13.hknm2', 'rb') as infile:
            header = havok.Header(infile)
            self.assertEqual(header.signature, b'W\xe0\xe0W\x10\xc0\xc0\x10')
            self.assertEqual(header.size, 80)
            self.assertEqual(header.version, 'hk_2014.2.0-r1')
