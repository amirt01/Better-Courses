from dataclasses import dataclass, field


@dataclass()
class Course:
    section: str = ''
    code: str = ''
    title: str = ''
    units: str = ''
    description: str = ''
    corequisites: list[str] = field(default_factory=list)
    prerequisites: list[str] = field(default_factory=list)
    name: str = field(init=False, hash=False, repr=False)

    def __post_init__(self) -> None:
        self.name = f'{self.section} {self.code}'

    def __dict__(self) -> dict:
        result = dict()
        for f in getattr(self, '__dataclass_fields__').values():
            value = getattr(self, f.name)
            if f.name != 'name':
                result[f.name] = value
        return result

    def __str__(self) -> str:
        return self.name


if __name__ == '__main__':
    import inspect

    print(*inspect.getmembers(Course, inspect.isfunction), sep='\n')
    print(Course().__dict__())
