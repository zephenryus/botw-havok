import unittest
import havok


class TestClassNames(unittest.TestCase):
    def test_class_names_can_be_decompiled_from_the_class_names_section(self):
        """ @test class names can be decompiled from the class names section
        Given the file Npc_King_Vagrant.hkcl
        When the file is passed to the ClassNames class
        Then the list of class names should be decompiled
        """

        with open('../assets/Npc_King_Vagrant.hkcl', 'rb') as infile:
            infile.seek(64)
            section_header_tables = havok.SectionHeaderTables(infile)
            classnames = havok.ClassNames(infile, section_header_tables.classnames)
            self.assertEqual(len(classnames), 30)
            self.assertEqual(classnames[0].name, 'hkClass')
            self.assertEqual(classnames[5].name, 'hclClothContainer')
