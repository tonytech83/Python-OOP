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
