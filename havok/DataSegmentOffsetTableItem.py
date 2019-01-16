class DataSegmentOffsetTableItem:
    def __init__(self, meta_offset, data_offset):
        self.meta = meta_offset
        self.data = data_offset

    def __repr__(self):
        return "{} <meta: {}, data: {}>".format(
            self.__class__.__name__,
            hex(self.meta),
            hex(self.data)
        )