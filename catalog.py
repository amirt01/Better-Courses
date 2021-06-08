import jsons

from dataclasses import asdict
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
        self.store[self._keytransform(course.section + ' ' + str(course.code))] = course

    def save_to_file(self, path: str):
        with open(path, 'w') as outfile:
            outfile.write(jsons.dumps(self.values()))

    def load_from_file(self, path: str):
        with open(path, 'r') as infile:
            for course in jsons.loads(infile.read(), cls=list[Course]):
                self.add(course)

    def _keytransform(self, key: str):
        return key.upper()

    def __str__(self):
        return '\n'.join(map(str, self.store))
