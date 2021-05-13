import jsons

from course import Course


class Catalog(dict):
    def __init__(self, path: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        if path:
            self.read_from_file(path)

    def insert(self, course: Course):
        self[str(course.section) + ' ' + str(course.code)] = course

    def save_to_file(self, path: str):
        with open(path, 'w') as outfile:
            outfile.write(jsons.dumps(self.values(), strip_privates=True))

    def read_from_file(self, path: str):
        with open(path, 'r') as infile:
            for course in jsons.loads(infile.read(), cls=list[Course]):
                self.insert(course)

    def __str__(self):
        return '\n\n'.join(map(str, self.values()))
