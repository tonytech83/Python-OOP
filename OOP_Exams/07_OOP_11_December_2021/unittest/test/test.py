from project.team import Team

from unittest import TestCase, main


class TeamTests(TestCase):

    def setUp(self) -> None:
        self.team = Team('CSKA')
        self.other_team = Team('Levski')

    def test_constructor(self):
        name = 'CSKA'

        m = Team(name)

        self.assertEqual(name, m.name)
        self.assertEqual({}, m.members)

    def test_name_setter_with_not_valid_data_raises(self):
        with self.assertRaises(ValueError) as er:
            self.team.name = 'CSKA 1948'

        self.assertEqual("Team Name can contain only letters!", str(er.exception))

    def test_add_member(self):
        name_age = {
            'Ivan': 18,
            'Stoqn': 19,
        }

        expected_return = 'Successfully added: Ivan, Stoqn'
        actual_return = self.team.add_member(**name_age)

        self.assertEqual(name_age, self.team.members)
        self.assertEqual(expected_return, actual_return)

        new_name_age = {
            'Ivan': 18,
            'Petar': 30,
        }

        expected_return = 'Successfully added: Petar'
        actual_return = self.team.add_member(**new_name_age)

        self.assertEqual({'Ivan': 18, 'Stoqn': 19, 'Petar': 30}, self.team.members)
        self.assertEqual(expected_return, actual_return)

    def test_remove_member_when_name_not_exists(self):
        name_age = {
            'Ivan': 18,
            'Stoqn': 19,
        }

        self.team.add_member(**name_age)
        self.assertEqual(name_age, self.team.members)

        actual_return = self.team.remove_member('Petar')

        self.assertEqual("Member with name Petar does not exist", actual_return)
        self.assertEqual(name_age, self.team.members)

    def test_remove_member_when_name_exists(self):
        name_age = {
            'Ivan': 18,
            'Stoqn': 19,
        }
        self.team.add_member(**name_age)
        self.assertEqual(name_age, self.team.members)

        expected_return = "Member Ivan removed"
        actual_return = self.team.remove_member('Ivan')

        self.assertEqual({'Stoqn': 19}, self.team.members)
        self.assertEqual(expected_return, actual_return)

    def test_gt_dunder(self):
        name_age = {
            'Ivan': 18,
            'Stoqn': 19,
        }

        self.team.add_member(**name_age)

        self.assertEqual(True, self.team > self.other_team)
        self.assertEqual(False, self.team < self.other_team)

    def test_len_dunder(self):
        self.assertEqual(0, self.team.__len__())
        self.assertEqual(0, self.other_team.__len__())

        self.team.add_member(Ivan=19)

        self.assertEqual(1, self.team.__len__())
        self.assertEqual(0, self.other_team.__len__())

    def test_add_dunder(self):
        self.team.add_member(Ivan=19)
        self.other_team.add_member(Stoqn=20)

        expected_new_name = 'CSKALevski'
        new_team = self.team + self.other_team

        self.assertEqual(expected_new_name, new_team.name)

        expected_new_members = {'Ivan': 19, 'Stoqn': 20}

        self.assertEqual(expected_new_members, new_team.members)

    def test_str_dunder_without_members(self):
        expected_return = f'Team name: CSKA'
        actual_result = self.team.__str__()

        self.assertEqual(expected_return, actual_result)

    def test_str_dunder_with_with_equal_ages(self):
        name_age = {
            'Stoqn': 18,
            'Ivan': 18,
        }
        self.team.add_member(**name_age)

        expected_return = f'Team name: CSKA\n' \
                          f'Member: Ivan - 18-years old\n' \
                          f'Member: Stoqn - 18-years old'
        actual_result = self.team.__str__()

        self.assertEqual(expected_return, actual_result)

    def test_str_dunder_with_different_ages(self):
        name_age = {
            'Stoqn': 18,
            'Ivan': 17,
        }

        self.team.add_member(**name_age)

        expected_return = f'Team name: CSKA\n' \
                          f'Member: Stoqn - 18-years old\n' \
                          f'Member: Ivan - 17-years old'
        actual_result = self.team.__str__()

        self.assertEqual(expected_return, actual_result)


if __name__ == '__main__':
    main()
