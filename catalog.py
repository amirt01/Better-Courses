import jsons

from course import Course


class Catalog:
    def __init__(self, path: str = None):
        self._catalog = {}
        if path:
            self.load_from_file(path)

    def add(self, course: Course):
        self._catalog[course.section + ' ' + str(course.code)] = course

    def save_to_file(self, path: str):
        with open(path, 'w') as outfile:
            outfile.write(jsons.dumps(self._catalog.values(), strip_privates=True))

    def load_from_file(self, path: str):
        with open(path, 'r') as infile:
            for course in jsons.loads(infile.read(), cls=list[Course]):
                self.add(course)

    def __str__(self):
        return '\n'.join(map(str, self._catalog))
