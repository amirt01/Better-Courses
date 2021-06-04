class Course:
    def __init__(self, section='', code=0, title='', units=0, description='', corequisites=None, prerequisites=None):
        self._section = str(section)
        try:
            self._code = int(code)
        except ValueError:
            self._code = str(code)
        self._title = str(title)
        try:
            self._units = int(units)
        except ValueError:
            self._units = str(units)
        self._description = str(description)
        self._corequisites = corequisites if corequisites else []
        self._prerequisites = prerequisites if prerequisites else []

    @property
    def name(self):
        return self._section + str(self._code)

    @property
    def section(self):
        return self._section

    @property
    def code(self):
        return self._code

    @property
    def title(self):
        return self._title

    @property
    def units(self):
        return self._units

    @property
    def description(self):
        return self._description

    @property
    def corequisites(self):
        return self._corequisites

    @property
    def prerequisites(self):
        return self._prerequisites

    @section.setter
    def section(self, new_section):
        self._section = new_section

    @code.setter
    def code(self, new_code):
        self._code = new_code

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @units.setter
    def units(self, new_units):
        self._units = new_units

    @description.setter
    def description(self, new_description):
        self._description = new_description

    def add_corequisite(self, corequisite):
        self._corequisites.append(corequisite)

    def remove_corequisite(self, corequisite):
        self._corequisites.remove(corequisite)

    def add_prerequisite(self, prerequisite):
        self._prerequisites.append(prerequisite)

    def remove_prerequisite(self, prerequisite):
        self._prerequisites.remove(prerequisite)

    def __str__(self):
        return str(self._section) + ' ' + str(self._code)

    def __repr__(self):
        return f'section: {self._section}\n' \
               f'code: {self._code}\n' \
               f'title: {self._title}\n' \
               f'units: {self._units}\n' \
               f'description: {self._description}\n' \
               f'prerequisites: {self._prerequisites}\n' \
               f'corequisites: {self._corequisites}'
