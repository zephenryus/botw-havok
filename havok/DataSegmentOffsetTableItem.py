class DataSegmentOffsetTableItem:
    meta: int
    data: int
    length: int

    def __init__(self, meta_offset: int, data_offset: int, length=0) -> None:
        self.meta = meta_offset
        self.data = data_offset
        self.length = length

    def __repr__(self):
        return "{} <meta: {}, data: {}>".format(
            self.__class__.__name__,
            hex(self.meta),
            hex(self.data)
        )