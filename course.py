from dataclasses import dataclass, field, asdict


@dataclass
class Course:
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


if __name__ == '__main__':
    import inspect

    print(*inspect.getmembers(Course, inspect.isfunction), sep='\n')
