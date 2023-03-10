from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = 200000
    sponsors = {
        'first_sponsor': {
            1: 1000000,
            3: 500000,
        },
        'second_sponsor': {
            5: 100000,
            7: 50000
        }
    }

    # def calculate_revenue_after_race(self, race_pos: int):
    #     # first_sponsors = {
    #     #     1: 1000000,
    #     #     3: 500000,
    #     # }
    #     # second_sponsor = {
    #     #     5: 100000,
    #     #     7: 50000
    #     # }
    #     #
    #     # first_sponsors_reward = max([first_sponsors[place] if race_pos <= place else 0 for place in first_sponsors])
    #     # second_sponsor_reward = max([second_sponsor[place] if race_pos <= place else 0 for place in second_sponsor])
    #     #
    #     # revenue = (first_sponsors_reward + second_sponsor_reward) - MercedesTeam.EXPENSES_PER_RACE
    #     # self.budget += revenue
    #     #
    #     # return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
    #     pass
