import random

class Commentary:
    '''Commentary class '''
    def __init__(self, umpire):
        self.umpire = umpire
        self.runs = 0

    def provide_commentary(self):
        '''Ball by ball descrption'''
        innings_count = 1
        batting_team, bowling_team = self.umpire.teams

        while innings_count <= 2:
            self.print_innings_header(
                innings_count, batting_team, 
                bowling_team)

            while (self.umpire.overs < 4 
                   and self.umpire.wickets[batting_team.name] < 10):
                self.print_over_header(self.umpire.overs)

                for ball in range(6):
                    decision, self.runs = self.umpire.simulate_ball()
                    self.print_ball_result()

                    if (self.umpire.wickets[batting_team.name] >= 10 
                            or self.umpire.overs >= 4):
                        break

                if (self.umpire.wickets[batting_team.name] >= 10 
                        or self.umpire.overs >= 4):
                    break

            if (self.umpire.wickets[batting_team.name] >= 10 
                    or self.umpire.balls >= 4):
                self.print_innings_summary(batting_team)
                innings_count += 1
                if innings_count > 2:
                    break
                self.print_innings_header(
                    innings_count, batting_team, 
                    bowling_team)
                self.umpire.end_innings(batting_team, 
                                        bowling_team)

    def print_innings_header(
            self, innings_count, 
            batting_team, 
            bowling_team):
        '''Inning  description at start'''
        print(f"\nInnings {innings_count}: {batting_team.name} vs {bowling_team.name}")

    def print_table_header(self):
        '''Headrs for description'''
        print("Over\t\tRuns\t\tScore\t\t\tCommentary")

    def print_over_header(self, over):
        print(f"\nOver {int(over)+1}:")
        self.print_table_header()

    def print_ball_commentary(
            self, over, 
            runs, commentary):
        '''Description of each ball'''
        if self.runs == -1:
            self.runs = 'W'
        print(f"{over}\t|\t{self.runs}\t|\t\t{self.umpire.runs[self.umpire.teams[0].name]}/{self.umpire.wickets[self.umpire.teams[0].name]}\t|\t{commentary}")

    def print_ball_result(self):
        '''Result generated from each ball used for description'''
        batting_team, bowling_team = self.umpire.teams
        total_runs = self.umpire.runs[batting_team.name]
        wickets = self.umpire.wickets[batting_team.name]
        commentary = self.generate_commentary(self.runs, wickets)
        over = f"{int(self.umpire.overs)}.{self.umpire.balls % 6 }"
        self.print_ball_commentary(over, total_runs, commentary)

    def generate_commentary(self, runs, wickets):
        '''Different commentary outputs depending on ball result'''
        if wickets >= 10:
            return "All out"
        elif runs == -1:
            outputs = [
                'Perfect yorker by bowler and batsman uunable to react OUT!!!',
                'Batsman tries to go for six but caught by fielder at mid on OUT!!!',
                'Slower ball batsman hits it straight to bowler OUT!!!',
                'Loose Shot by batsman and he is OUT!!!!'
                ]
            return random.choice(outputs)
        elif runs == 4:
            outputs = [
                'Exquisite shot by batsman for a boundary',
                'Puched down the ground for 4',
                'Classic cuvre drive by batsman for 4',
                'Loose ball by bowler and nailed for 4'
                ]
            return random.choice(outputs)
        elif runs == 6:
            outputs = [
                'Powerful shot by batsman for a 6',
                'Hammered straight over bowlers head for 6',
                'Perfectly executed hook shot by batsman for 6',
                'Loose ball by bowler and nailed for 6'
                ]
            return random.choice(outputs)
        elif runs == 0:
            outputs = [
                "That's a dot ball",
                "Batsman Fooled by the bowler! no run",
                "Mistimed shot stright to fielder no run",
                ]
            return random.choice(outputs)
        else:
            return "Tucked away by batsman for easy runs"

    def print_innings_summary(self, batting_team):
        '''Summary of each innings after completion'''
        print(f"\nInnings Summary: {batting_team.name} - {self.umpire.runs[batting_team.name]}/{self.umpire.wickets[batting_team.name]}")
