from dataclasses import dataclass, field, asdict

class NodeMixin:
    def __children(self):
        try:
            return self._children
        except AttributeError:
            self._children = []
            return self._children

    @property
    def children(self):
        return tuple(self.__children())

    def add_child(self, new_child):
        if new_child is not None and not isinstance(new_child, NodeMixin):
            raise RuntimeError(f"Child node {new_child} is not of type 'NodeMixin'.")
        if new_child is self:
            raise RuntimeError(f"Cannot set Child. {self} cannot be a child of itself.")

        self.__children().append(new_child)

    @property
    def height(self):
        children = self.__children()
        if children:
            return max(child.height for child in children) + 1
        else:
            return 0


@dataclass
class Course(NodeMixin):
    section: str = ''
    code: str = ''
    title: str = ''
    units: str = ''
    description: str = ''
    corequisites: list[str] = field(default_factory=list)
    prerequisites: list[str] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self.section + ' ' + self.code

    def __dict__(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        return self.name

    def build_tree(self, cat):
        for prerequisite in self.prerequisites:
            try:
                self.add_child(cat[prerequisite])
            except (KeyError, TypeError):
                # print(f'{prerequisite} not found')
                continue
            except RuntimeError as re:
                print(re)


class RenderTree:
    def __init__(self, node):
        self.node = node
        self.seen = set()

    def __iter__(self):
        return self.__next(self.node, tuple())

    def __next(self, node, continues):
        if id(node) in self.seen:
            return
        else:
            self.seen.add(id(node))

        if not continues:  # if there's nothing to print
            yield '', node  # yield nothing
        else:
            shapes = ['│   ' if cont else '    ' for cont in continues]  # build all the shapes
            indent = ''.join(shapes[:-1])  # everything but the last one is part of the indent
            branch = '├── ' if continues[-1] else '└── '  # this is based on if it is the last child
            prefix = indent + branch
            yield prefix, node

        for i, child in enumerate(node.children):
            for grandchild in self.__next(child, continues + (i != len(node.children) - 1, )):
                yield grandchild