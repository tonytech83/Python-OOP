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
