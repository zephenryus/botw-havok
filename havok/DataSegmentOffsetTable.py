from havok import DataSegmentOffsetTableItem


class DataSegmentOffsetTable:
    def __init__(self):
        self.items = []

    def append(self, data: DataSegmentOffsetTableItem):
        self.items.append(data)

    def __repr__(self):
        return "{} <items: {}>".format(
            self.__class__.__name__,
            ', '.join(map(repr, self.items))
        )
