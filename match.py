from umpire import Umpire
from commentators import Commentary

class Match:
    '''Match simulation class'''
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = None
        self.commentary = None
        print(team1, team2)
        self.runs = {team1.name: 0, team2.name: 0}
        self.wickets = {team1.name: 0, team2.name: 0}

    def start_match(self):
        '''Simulation of match'''
        self.umpire = Umpire([self.team1, self.team2], self.field, self.runs, self.wickets)
        self.commentary = Commentary(self.umpire)
        self.commentary.provide_commentary()

    def simulate_match(self):
        '''For binding match simulation and winning teams'''
        self.start_match()
        winning_team = self.end_match()
        return winning_team

    def end_match(self):
        '''Method for match end, switching the innings and determination of winner'''
        batting_team = self.team1 if self.wickets[self.team1.name] >= 10 else self.team2
        bowling_team = self.team2 if batting_team == self.team1 else self.team1

        if self.runs[batting_team.name] > self.runs[bowling_team.name]:
            winning_team = batting_team
        elif self.runs[bowling_team.name] > self.runs[batting_team.name]:
            winning_team = bowling_team
        else:
            winning_team = None

        if winning_team:
            print(f"\nMatch Summary: {batting_team.name} vs {bowling_team.name}")
            print(f"{batting_team.name}: {self.runs[batting_team.name]}/{self.wickets[batting_team.name]}")
            print(f"{bowling_team.name}: {self.runs[bowling_team.name]}/{self.wickets[bowling_team.name]}")
            print(f"Winner: {winning_team.name}")
        else:
            print("\nThe match ended in a tie.")
            
        return winning_team