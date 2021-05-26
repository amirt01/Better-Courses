import jsons

from course import Course


class Catalog(dict):
    def __init__(self, path: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        if path:
            self.load_from_file(path)

    def add(self, course: Course):
        self[course.section + ' ' + str(course.code)] = course

    def save_to_file(self, path: str):
        with open(path, 'w') as outfile:
            outfile.write(jsons.dumps(self, strip_privates=True))

    def load_from_file(self, path: str):
        with open(path, 'r') as infile:
            for course in jsons.loads(infile.read(), cls=dict[str, Course]).values():
                self.add(course)

    def __str__(self):
        return '\n'.join(map(str, self))
