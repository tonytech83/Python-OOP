from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):
    student = Student('Ivan', {'Python': ['some note']})

    def test_class_constructor(self):
        for course in [{'Python': ['some note']}, None]:
            name = 'Ivan'
            courses = {} if course is None else course

            student = Student(name, courses)

            self.assertEqual(name, student.name)
            self.assertEqual(courses, student.courses)

    def test_enroll_method_when_course_name_appear_in_courses(self):
        expected_notes = ['some note', 'first note']
        expected_return = 'Course already added. Notes have been updated.'

        actual_return = self.student.enroll('Python', ['first note'])
        actual_notes = self.student.courses['Python']

        self.assertEqual(expected_notes, actual_notes)
        self.assertEqual(expected_return, actual_return)

    def test_enroll_method_when_add_course_notes_is_y(self):
        expected_return = 'Course and course notes have been added.'
        expected_notes = ['new note']

        actual_return = self.student.enroll('C#', ['new note'], 'Y')
        actual_notes = self.student.courses['C#']

        self.assertEqual(expected_notes, actual_notes)
        self.assertEqual(expected_return, actual_return)

    def test_enroll_method_when_add_course_notes_is_empty_string(self):
        expected_return = 'Course and course notes have been added.'
        expected_notes = ['new note']

        actual_return = self.student.enroll('Ruby', ['new note'])
        actual_notes = self.student.courses['Ruby']

        self.assertEqual(expected_notes, actual_notes)
        self.assertEqual(expected_return, actual_return)

    def test_enroll_method_when_add_course_notes_is_different_from_y_or_empty_string(self):
        expected_result = 'Course has been added.'
        expected_notes = []

        actual_return = self.student.enroll('Java', ['new note'], 'Z')
        actual_notes = self.student.courses['Java']

        self.assertEqual(expected_notes, actual_notes)
        self.assertEqual(expected_result, actual_return)

    def test_add_notes_when_course_name_in_student_courses(self):
        student = Student('Ivan', {'Python': ['some note']})
        expected_return = 'Notes have been updated'
        expected_notes = ['some note', 'this note']

        actual_return = student.add_notes('Python', 'this note')
        actual_notes = student.courses['Python']

        self.assertEqual(expected_notes, actual_notes)
        self.assertEqual(expected_return, actual_return)

    def test_add_notes_when_course_name_not_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('C#', 'this note')

        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leave_course_when_course_in_student_courses(self):
        student = Student('Ivan', {'Python': ['some note']})
        actual_return = student.leave_course('Python')

        expected_return = 'Course has been removed'
        expected_courses = {}
        actual_courses = student.courses

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_courses, actual_courses)

    def test_leave_course_when_course_not_in_student_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Java Script')

        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == '__main__':
    main()
