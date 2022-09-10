class team_information_entity():
    def __init__(self, team) -> None:
        self.team = team
        self.goals = 0
        self.wins = 0
        self.draws = 0
        self.losts = 0

    def json(self):
        return {"team": self.team, "goals": self.goals, "wins": self.wins, "draws": self.draws, "losts": self.losts}

    def __repr__(self):
        return f"Team Information Obj: {{{self.team}, goals: {self.goals}, wins: {self.wins}, draws: {self.draws}, losts: {self.losts}}}"