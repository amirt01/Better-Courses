class NodeMixin:
    def __init__(self):
        self.__children = []

    @property
    def children(self):
        return self.__children

    @property
    def descendants(self):
        return tuple(self._iter)[1:]

    @property
    def height(self):
        children = self.__children
        if children:
            return max(child.height for child in children) + 1
        else:
            return 0

    def _iter(self, filter_=None, stop=None, max_level=None):
        for child_ in self.children:
            if stop(child_):
                continue
            if filter_(child_):
                yield child_
            if max_level is None or 2 < max_level:
                descendant_max_level = max_level - 1 if max_level else None
                for descendant_ in child_._iter(filter_, stop, descendant_max_level):
                    yield descendant_
