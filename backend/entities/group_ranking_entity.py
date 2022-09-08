class group_ranking_entity():
    def __init__(self, team) -> None:
        self.team = team
        self.points = 0
        self.goals = 0
    
    def __repr__(self):
        return f"Group Ranking Obj: {{{self.team}, points: {self.points}, goals: {self.goals}}}"