from collections.abc import Mapping


class AttributeMap(Mapping):
    """
    Abstract Methods: __getitem__, __iter__, and __len__
    Mixin Methods: __contains__, keys, items, values, get, __eq__, and __ne__
    """

    def __init__(self, key_attribute, key_transform=lambda key: key):
        self._storage = dict()
        self._key_attribute = key_attribute
        self._key_transform = key_transform

    def __getitem__(self, key: str):
        return self._storage[self._key_transform(key)]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)

    def _key_maker(self, value):
        return self._key_transform(value.__dict__()[self._key_attribute])

    def add(self, course):
        key = self._key_maker(course)
        self._storage[key] = course
        return key


if __name__ == '__main__':
    import inspect

    print(*inspect.getmembers(AttributeMap, inspect.isfunction), sep='\n')
