import random

class Umpire:
    '''Umpire class '''
    def __init__(
            self, teams, 
            field, runs, 
            wickets):
        self.teams = teams
        self.field = field
        self.runs = runs
        self.wickets = wickets
        self.overs = 0
        self.balls = 0

    def simulate_ball(self):
        '''Ball simulation based on probablity'''
        batting_team, bowling_team = self.teams

        batsman = batting_team.send_next_player()
        bowler = bowling_team.choose_bowler()

        boundary_probability = self.field.calculate_boundary_probability(
                                sum(player.fielding_stats for player in bowling_team.players))
        run_probability = self.field.calculate_run_probability(
                                sum(player.fielding_stats for player in bowling_team.players))

        score = batsman.calculate_score()
        decision = self.make_decision(score, boundary_probability, run_probability, bowler.bowling_stats)
        #print(decision, '£££' , score, '££££', boundary_probability, '££££', run_probability,' -----')

        if decision == 'out':
            self.wickets[batting_team.name] += 1
            if self.wickets[batting_team.name] >= 10:
                self.end_innings(batting_team, bowling_team)
            runs = -1
        elif decision == 'boundary':
            runs = random.choices([4, 6], weights=[0.7, 0.3], k=1)[0]
            self.runs[batting_team.name] += runs
        elif decision == 'run':
            runs = random.choices([1, 2, 3, 5], weights=[0.4, 0.3, 0.2, 0.1], k=1)[0]
            self.runs[batting_team.name] += runs
        elif decision == 'wide':
            self.runs[batting_team.name] += 1
        elif decision == 'no_ball':
            runs = random.choices([1, 2, 3, 4, 6], weights=[0.4, 0.3, 0.15, 0.05, 0.1], k=1)[0]
            self.runs[batting_team.name] += runs + 1
        elif decision == 'no_run':
            runs = 0
        

        if decision not in ['wide','no_ball']:
            self.balls += 1
            if self.balls % 6 == 0:
                self.overs += 1
                
        return decision, runs

    def make_decision(
            self, score, 
            boundary_probability, 
            run_probability, 
            bowling_stats):
        '''Decision for each ball is made here'''
        max_score = max(boundary_probability, run_probability, bowling_stats)
        probabilities = [
            boundary_probability / max_score,
            run_probability / max_score,
            bowling_stats / max_score,
            (1 - max_score)  # Wicket-taking probability
        ]
        decision = random.choices(['boundary', 'run', 'no_run', 'out'], weights=probabilities, k=1)[0]
        return decision

    def end_innings(
            self, batting_team, 
            bowling_team):
        '''Inning end change of teams'''
        batting_team, bowling_team = bowling_team, batting_team
        self.teams = [batting_team, bowling_team]
        self.overs = 0
        self.balls = 0
