class SectionHeaderItem(object):
    rel_offset: int
    abs_offset: int
    size: int

    def __init__(self, rel_offset: int, abs_offset: int, length: int):
        self.rel_offset = rel_offset
        self.abs_offset = abs_offset
        self.size = length

    def __repr__(self):
        return "{} <rel_offset: {}, abs_offset: {}, size: {}>".format(
            self.__class__.__name__,
            hex(self.rel_offset),
            hex(self.abs_offset),
            self.size
        )