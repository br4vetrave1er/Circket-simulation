from players import Player
import random
from team import Team


class Player_data:
    def __init__(self):
        
        #Indian team
        self.indian_players = [
            ("Virat Kohli", 0.95, 0.15, 0.85, 0.95, 0.90),  # Batsman
            ("Rohit Sharma", 0.90, 0.10, 0.80, 0.85, 0.85),  # Batsman
            ("Jasprit Bumrah", 0.05, 0.90, 0.90, 0.80, 0.85),  # Bowler
            ("Ravindra Jadeja", 0.70, 0.85, 0.90, 0.90, 0.80),  # All-rounder
            ("KL Rahul", 0.85, 0.10, 0.80, 0.90, 0.85),  # Batsman
            ("Hardik Pandya", 0.80, 0.80, 0.85, 0.90, 0.85),  # All-rounder
            ("Rishabh Pant", 0.85, 0.15, 0.80, 0.85, 0.80),  # Batsman
            ("Ravichandran Ashwin", 0.60, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Mohammed Shami", 0.10, 0.85, 0.90, 0.70, 0.80),  # Bowler
            ("Yuzvendra Chahal", 0.60, 0.85, 0.90, 0.70, 0.80),  # Bowler
            ("Ajinkya Rahane", 0.80, 0.10, 0.80, 0.85, 0.80),  # Batsman
            
        ]


        # Australia Team
        self.australia_players = [
            ("David Warner", 0.90, 0.10, 0.80, 0.85, 0.85),  # Batsman
            ("Steve Smith", 0.95, 0.05, 0.80, 0.85, 0.85),  # Batsman
            ("Mitchell Starc", 0.10, 0.90, 0.90, 0.75, 0.85),  # Bowler
            ("Glenn Maxwell", 0.80, 0.85, 0.90, 0.90, 0.80),  # All-rounder
            ("Aaron Finch", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Pat Cummins", 0.10, 0.90, 0.85, 0.75, 0.80),  # Bowler
            ("Alex Carey", 0.80, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Adam Zampa", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("Nathan Lyon", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("Usman Khawaja", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Glenn Phillips", 0.80, 0.85, 0.85, 0.80, 0.80),  # All-rounder
        ]

        # England Team
        self.england_players = [
            ("Eoin Morgan", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Joe Root", 0.90, 0.10, 0.80, 0.85, 0.85),  # Batsman
            ("Jofra Archer", 0.10, 0.90, 0.85, 0.80, 0.85),  # Bowler
            ("Ben Stokes", 0.85, 0.85, 0.85, 0.90, 0.85),  # All-rounder
            ("Jonny Bairstow", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Chris Woakes", 0.70, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Jos Buttler", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Adil Rashid", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("Mark Wood", 0.10, 0.90, 0.85, 0.75, 0.80),  # Bowler
            ("Jason Roy", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Sam Curran", 0.80, 0.85, 0.85, 0.80, 0.80),  # All-rounder
        ]

        # New Zealand Team
        self.new_zealand_players = [
            ("Kane Williamson", 0.90, 0.10, 0.80, 0.85, 0.85),  # Batsman
            ("Trent Boult", 0.10, 0.90, 0.90, 0.75, 0.85),  # Bowler
            ("Martin Guptill", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Ross Taylor", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Lockie Ferguson", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("James Neesham", 0.80, 0.85, 0.85, 0.90, 0.80),  # All-rounder
            ("Tom Latham", 0.80, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Mitchell Santner", 0.60, 0.85, 0.85, 0.75, 0.80),  # All-rounder
            ("Ish Sodhi", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("Colin de Grandhomme", 0.80, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Tim Southee", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
        ]

        # Pakistan Team
        self.pakistan_players = [
            ("Babar Azam", 0.90, 0.10, 0.80, 0.85, 0.85),  # Batsman
            ("Shaheen Afridi", 0.10, 0.90, 0.90, 0.75, 0.85),  # Bowler
            ("Fakhar Zaman", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Shadab Khan", 0.70, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Imad Wasim", 0.70, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Mohammad Hafeez", 0.80, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Mohammad Rizwan", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Haris Rauf", 0.10, 0.90, 0.85, 0.75, 0.80),  # Bowler
            ("Hasan Ali", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("Shoaib Malik", 0.80, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Asif Ali", 0.80, 0.85, 0.85, 0.80, 0.80),  # All-rounder
        ]

        # Sri Lanka Team
        self.srilanka_players = [
            ("Kusal Perera", 0.90, 0.10, 0.80, 0.85, 0.85),  # Batsman
            ("Lasith Malinga", 0.10, 0.90, 0.90, 0.75, 0.85),  # Bowler
            ("Angelo Mathews", 0.85, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Dimuth Karunaratne", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Dhananjaya de Silva", 0.70, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Isuru Udana", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("Avishka Fernando", 0.85, 0.10, 0.80, 0.85, 0.80),  # Batsman
            ("Wanindu Hasaranga", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("Kasun Rajitha", 0.10, 0.85, 0.85, 0.75, 0.80),  # Bowler
            ("Bhanuka Rajapaksa", 0.80, 0.85, 0.85, 0.80, 0.80),  # All-rounder
            ("Lahiru Kumara", 0.10, 0.90, 0.85, 0.75, 0.80),  # Bowler
        ]

    def create_player(self):
        # Create players using improved data
        self.indian_players = [Player(*data) for data in self.indian_players]
        self.australia_players = [Player(*data) for data in self.australia_players]
        self.england_players = [Player(*data) for data in self.england_players]
        self.new_zealand_players = [Player(*data) for data in self.new_zealand_players]
        self.pakistan_players = [Player(*data) for data in self.pakistan_players]
        self.srilanka_players = [Player(*data) for data in self.srilanka_players]


    def create_teams(self):
        # Form teams using the players
        self.indian_team = Team("India", self.indian_players[:11])
        self.australia_team = Team("Australia", self.australia_players[:11])
        self.england_team = Team("England", self.england_players[:11])
        self.new_zealand_team = Team("New Zealand", self.new_zealand_players[:11])
        self.pakistan_team = Team("Pakistan", self.pakistan_players[:11])
        self.srilanka_team = Team("Sri Lanka", self.srilanka_players[:11])

    def available_teams(self):
        self.create_player()
        self.create_teams()
        # Available teams for the tournament
        teams = [self.australia_team, self.england_team, self.new_zealand_team, self.pakistan_team, self.srilanka_team]
        
        return teams

