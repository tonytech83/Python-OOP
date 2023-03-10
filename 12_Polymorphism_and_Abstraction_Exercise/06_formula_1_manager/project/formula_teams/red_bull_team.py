from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250000
    sponsors = {
        'first_sponsor': {
            1: 1500000,
            2: 800000,
        },
        'second_sponsor': {
            8: 20000,
            10: 10000
        }
    }

    # def calculate_revenue_after_race(self, race_pos: int):
        # first_sponsors = {
        #     1: 1500000,
        #     2: 800000,
        # }
        # second_sponsor = {
        #     8: 20000,
        #     10: 10000
        # }
        #
        # first_sponsors_reward = max([first_sponsors[place] if race_pos <= place else 0 for place in first_sponsors])
        # second_sponsor_reward = max([second_sponsor[place] if race_pos <= place else 0 for place in second_sponsor])
        #
        # revenue = (first_sponsors_reward + second_sponsor_reward) - RedBullTeam.EXPENSES_PER_RACE
        # self.budget += revenue
        #
        # return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
        # pass
