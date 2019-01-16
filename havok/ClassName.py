class ClassName(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "{} <id: {}, name: '{}'>".format(self.__class__.__name__, self.id, self.name)

    def __str__(self):
        return self.__repr__()
