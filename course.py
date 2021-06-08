from dataclasses import dataclass


@dataclass
class Course:
    section: str
    code: str
    title: str
    units: str
    description: str
    corequisites: list
    prerequisites: list

    def __str__(self):
        return f'{self.section} {self.code}'
