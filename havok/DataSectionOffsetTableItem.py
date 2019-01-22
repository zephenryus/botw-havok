class DataSectionOffsetTableItem(object):
    meta: int
    data: int
    size: int
    array_length: int

    def __init__(self, meta_offset: int, data_offset: int, size=0, array_length=0) -> None:
        self.meta = meta_offset
        self.data = data_offset
        self.size = size
        self.array_length = array_length

    def __repr__(self):
        return "{} <meta: {}, data: {}, size: {}, array_length: {}>".format(
            self.__class__.__name__,
            hex(self.meta),
            hex(self.data),
            self.size,
            self.array_length
        )