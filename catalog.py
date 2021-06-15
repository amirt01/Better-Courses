import json

from course import Course
from attribute_map import AttributeMap


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


if __name__ == '__main__':
    import inspect

    print(*inspect.getmembers(Catalog, inspect.isfunction), sep='\n')
