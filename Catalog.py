from collections.abc import Mapping


class AttributeMap(Mapping):
    """
    Abstract Methods: __getitem__, __iter__, and __len__
    Mixin Methods: __contains__, keys, items, values, get, __eq__, and __ne__
    """

    def __init__(self, key_attribute, key_transform=lambda key: key):
        """
        :param key_attribute: the attribute to be used as the key
        :param key_transform: any transformation to be done to the key (identity by default)
        """
        self._storage = dict()
        self._key_attribute = key_attribute
        self._key_transform = key_transform

    def __getitem__(self, key: str):
        return self._storage[self._key_transform(key)]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self) -> int:
        return len(self._storage)

    def _key_maker(self, value):
        return self._key_transform(getattr(value, self._key_attribute))

    def add(self, course):
        self._storage[self._key_maker(course)] = course

    def __repr__(self):
        return f'{type(self).__name__}(key_attribute={self._key_attribute}, key_transform={self._key_transform}, len={len(self)})'


class Catalog(AttributeMap):
    def __init__(self, path: str = None):
        super().__init__(key_attribute='name', key_transform=str.upper)
        if path:
            self.load_from_file(path)

    def save_to_file(self, path: str):
        with open(path, 'w') as outfile:
            outfile.write(json.dumps([course.__dict__() for course in self.values()]))

    def load_from_file(self, path: str):
        with open(path, 'r') as infile:
            for course_dict in json.loads(infile.read()):
                self.add(Course(*course_dict.values()))
