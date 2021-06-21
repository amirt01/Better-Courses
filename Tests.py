from unittest import TestCase
from Course import Course
from Catalog import Catalog


class CourseTestCase(TestCase):
    def setUp(self) -> None:
        self.section = 'ENGRMAE'
        self.code = '135'
        self.title = 'Compressible Flow'
        self.units = '4'
        self.prerequisites = ['ENGRMAE 130A']

    def assertCourse(self, course):
        self.assertEqual(course.section, self.section)
        self.assertEqual(course.code, self.code)
        self.assertEqual(course.title, self.title)
        self.assertEqual(course.units, self.units)
        self.assertEqual(course.prerequisites, self.prerequisites)

    def testInit(self):
        course = Course(self.section, self.code, self.title, self.units, prerequisites=self.prerequisites)
        self.assertCourse(course)

    def testAssign(self):
        course = Course()

        course.section = 'ENGRMAE'
        course.code = '135'
        course.title = 'Compressible Flow'
        course.units = '4'
        course.prerequisites = ['ENGRMAE 130A']

        self.assertCourse(course)

    def testName(self):
        course = Course(self.section, self.code)
        self.assertEqual(course.name, self.section + ' ' + self.code)

    def testEquality(self):
        course_a = Course(self.section, self.code, self.title, self.units, prerequisites=self.prerequisites)
        course_b = Course(self.section, self.code, self.title, self.units, prerequisites=self.prerequisites)
        self.assertEqual(course_a, course_b)

    def testNodeErrors(self):
        course_a = Course(self.section, self.code, self.title, self.units, prerequisites=self.prerequisites)
        with self.assertRaises(RuntimeError):
            course_a.add_child(course_a)

        with self.assertRaises(RuntimeError):
            course_a.add_child('test')


class CatalogTestCase(TestCase):
    def setUp(self) -> None:
        self.engrmae_135 = Course('ENGRMAE', '135', 'Compressible Flow', '4', prerequisites=['ENGRMAE 130A'])
        self.engrmae_147 = Course('ENGRMAE', '147', 'Vibrations', '4', prerequisites=['MATH 2E', 'MATH 3D'])

    def testLookup(self):
        catalog = Catalog()

        catalog.add(self.engrmae_135)
        catalog.add(self.engrmae_147)

        self.assertEqual(catalog['engrmae 135'], self.engrmae_135)
        self.assertEqual(catalog['engrmae 147'], self.engrmae_147)

        with self.assertRaises(KeyError):
            _ = catalog['test']
