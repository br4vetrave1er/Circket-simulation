import random
from match import Match
from players import Player
from team import Team
from field import Field
from playerdata import Player_data

class Tournament:
    '''Tournament class for simulation'''    
    
    def __init__(
            self, teams,
            field):
        self.teams = teams
        self.field = field
        self.round_names = {
            2: "Final",
            3: "Eliminator",
            4: "Semi Final",
            5: "Quater Final",
            6: "Quater Final"
        }
        self.selected_teams = []
        self.bracket = None
        
    def start(self):
        '''Method for the start of the tournament'''
        print("Welcome to the Tournament!")
        print("Available Teams:")
        self.print_available_teams()
        self.select_teams()
        self.check_odd_teams(self.selected_teams)
        self.generate_bracket(self.selected_teams)
        self.play_tournament()

    def print_available_teams(self):
        '''List all the available teams for the tournament'''
        for index, team in enumerate(self.teams):
            print(f"{index + 1}. {team.name}")

    def select_teams(self):
        '''Method for selection of teams to play tournamet'''
        num_teams = int(input("Enter the number of teams to select: "))
        for i in range(num_teams):
            team_index = int(input(f"Select team {i + 1}: "))
            if (team_index >= 1 
                    and team_index <= len(self.teams)):
                selected_team = self.teams[team_index - 1]
                self.selected_teams.append(selected_team)
                print(f"Team {selected_team.name} selected.")
            else:
                print("Invalid team index. Please try again.")
                return self.select_teams()
    
    def generate_bracket(self, randomteams):
        '''Bracket generation before the start of tournament'''
        num_teams = len(randomteams)
        num_matches = num_teams // 2
        self.bracket = [[] for _ in range(num_matches)]

        random.shuffle(randomteams)

        for i in range(num_matches):
            team1 = randomteams[i]
            team2 = randomteams[i + num_matches]
            match = (team1, team2)
            self.bracket[i].append(match)
        self.print_bracket(num_teams)
    
    
    def check_odd_teams(
            self, 
            teamlist):
        ''' 
        Check for odd teams as 1 team recives bye because 
        tournament uses single elimination bracket
        '''
        self.winners = []
        if (len(teamlist) % 2 != 0):
            bye_team = random.choice(teamlist)
            teamlist.remove(bye_team)
            print(f"\n\n{bye_team.name} has received a bye.")
            self.winners.append(bye_team)

    def play_tournament(self):
        '''For the start of tournament'''
        print("\nTournament started!")
        i = 1
        winners = self.winners.copy()
        while True:
            for match_round in self.bracket:
                
                
                for match in match_round:
                    winner = self.play_match(match)     # For the simulation of each match
                    winners.append(winner)
                
            self.bracket.clear()
            if (len(winners) != 1):
                self.check_odd_teams(winners)
                self.generate_bracket(winners)
                i + 1
                winners.clear()
                winners = self.winners.copy()
                continue
            else:
                break
                    
        print("\nTournament ended!")
        champion = winners[0]
        print(f"The champion of the tournament is {champion.name}!")

    def play_match(self, match):
        '''Simulation of every match done from this method'''
        team1, team2 = match
        current_match = Match(team1, team2, field)         # Here Simultion srcipt present in Match file is used
        winner = current_match.simulate_match()
        print(f"{team1.name} vs {team2.name} - Winner: {winner.name}")
        return winner

    def get_round_name(self, num_teams):
        '''Naming of each round based on number of teams present n tournament'''
        round_name = self.round_names.get(num_teams)
        if not round_name:
            round_name = f"Round {num_teams + 1}"
        return round_name
    
    def print_bracket(self, num_teams):
        '''Output of brackets for the next round'''
        print("\nTournament Bracket:")
        for match_round in self.bracket:
            round_name = self.get_round_name(num_teams)
            print(f"\n{round_name}:")
            for match in match_round:
                team1, team2 = match
                print(f"{team1.name} ------|")
                print(f"          |----- {round_name} Matchup ----|")
                print(f"{team2.name} ------|")
                print("")





# Form teams using the shuffled players
data = Player_data()
# Available teams for the tournament
teams = data.available_teams()

# Create an instance of field
field = Field()

# Create a tournament and play it
tournament = Tournament(teams, field)
tournament.start()