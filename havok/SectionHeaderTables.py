from typing import BinaryIO

from .SectionHeader import SectionHeader


class SectionHeaderTables(object):
    classnames: SectionHeader
    types: SectionHeader
    data: SectionHeader

    """ SectionHeaderTables
    Acts as a root container for the three available section offset tables in the Havok file
    """
    def __init__(self, infile: BinaryIO, file_start=0) -> None:
        self.classnames = SectionHeader(infile, file_start)
        self.types = SectionHeader(infile, file_start)
        self.data = SectionHeader(infile, file_start)

    def __repr__(self):
        return "{} <classnames: {}, types: {}, data: {}>".format(
            self.__class__.__name__,
            self.classnames,
            self.types,
            self.data,
        )

    def __str__(self):
        return self.__repr__()
