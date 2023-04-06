from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class StudentReportCardTests(TestCase):

    def setUp(self) -> None:
        self.src = StudentReportCard('Ivan', 6)

    def test_constructor(self):
        student_name = 'Ivan'
        school_year = 6

        src = StudentReportCard(student_name, school_year)

        self.assertEqual(student_name, src.student_name)
        self.assertEqual(school_year, src.school_year)
        self.assertEqual({}, src.grades_by_subject)

    def test_student_name_setter(self):
        self.src.student_name = 'Stoqn'

        self.assertEqual('Stoqn', self.src.student_name)

    def test_school_year_setter(self):
        self.src.school_year = 1

        self.assertEqual(1, self.src.school_year)

        self.src.school_year = 12

        self.assertEqual(12, self.src.school_year)

    def test_student_name_with_not_valid_data_raises(self):
        with self.assertRaises(ValueError) as er:
            self.src.student_name = ''

        self.assertEqual("Student Name cannot be an empty string!", str(er.exception))

    def test_school_year_with_negative_raises(self):
        with self.assertRaises(ValueError) as er:
            self.src.school_year = -1

        self.assertEqual("School Year must be between 1 and 12!", str(er.exception))

    def test_school_year_with_zero_raises(self):
        with self.assertRaises(ValueError) as er:
            self.src.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(er.exception))

    def test_school_year_with_bigger_than_twelve_raises(self):
        with self.assertRaises(ValueError) as er:
            self.src.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(er.exception))

    def test_add_grade_method(self):
        self.assertEqual({}, self.src.grades_by_subject)

        self.src.add_grade('A', 4)
        self.src.add_grade('A', 6)
        self.src.add_grade('B', 5)

        self.assertEqual({'A': [4, 6], 'B': [5]}, self.src.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.assertEqual('', self.src.average_grade_by_subject())

        self.src.add_grade('A', 4)
        self.src.add_grade('A', 6)
        self.src.add_grade('B', 1)

        self.assertEqual("A: 5.00\nB: 1.00", self.src.average_grade_by_subject())

        self.src.add_grade('A', 5)

        self.assertEqual("A: 5.00\nB: 1.00", self.src.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.src.add_grade('A', 4)
        self.src.add_grade('A', 6)

        self.assertEqual("Average Grade: 5.00", self.src.average_grade_for_all_subjects())

        self.src.add_grade('B', 2)

        self.assertEqual("Average Grade: 4.00", self.src.average_grade_for_all_subjects())

    def test_repr_dunder(self):
        self.src.add_grade('A', 4)

        expected_return = f"Name: Ivan\n" \
                          f"Year: 6\n" \
                          f"----------\n" \
                          f"A: 4.00\n" \
                          f"----------\n" \
                          f"Average Grade: 4.00"

        self.assertEqual(expected_return, repr(self.src))


if __name__ == '__main__':
    main()
