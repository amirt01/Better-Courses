import json

from course import Course
from collections.abc import Mapping


class Catalog(Mapping):
    def __init__(self, path: str = None):
        self.store = dict()
        if path:
            self.load_from_file(path)

    def __getitem__(self, key: str):
        return self.store[self._keytransform(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def add(self, course: Course):
        self.store[self._keytransform(str(course))] = course

    def save_to_file(self, path: str):
        with open(path, 'w') as outfile:
            outfile.write(json.dumps([course.__dict__() for course in self.values()]))

    def load_from_file(self, path: str):
        with open(path, 'r') as infile:
            for course_dict in json.loads(infile.read()):
                self.add(Course(*course_dict.values()))

    def _keytransform(self, key: str):
        return key.upper()

    def __str__(self):
        return '\n'.join(map(str, self.store))
