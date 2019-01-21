from typing import BinaryIO

from .SectionHeader import SectionHeader


class SectionHeaderTables(object):
    """ SectionHeaderTables
    Acts as a root container for the three available section offset tables in the Havok file
    """
    def __init__(self, infile: BinaryIO) -> None:
        self.classnames = SectionHeader(infile)
        self.types = SectionHeader(infile)
        self.data = SectionHeader(infile)

    def __repr__(self):
        return "{} <classnames: {}, types: {}, data: {}>".format(
            self.__class__.__name__,
            self.classnames,
            self.types,
            self.data,
        )

    def __str__(self):
        return self.__repr__()
