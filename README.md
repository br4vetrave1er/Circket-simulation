# Circket-simulation

This program simulates the cricket tournament played using the custom teams developed using advanced stats. The program mimics the real world cricket matches and stats. Program is developed using the python language

## Overview

The program consists of following files 
 1. `tournament` : This file is the main file used to simulate the tournament. This file has following important methods
    * `start` : this fuction is used to start the program 
    * `print_available_teams` : shows the teams available for user to select which are created using the player data
    * `generate_bracket` : Used to create the bracket format for the teams selected by the user.
    * `play_tournament` : The tournament is simulated using this method
    * `play_match` : For the smulation of each match
 
 2. `team` : This file has `Team` class which is used to create different teams. with methods for selecting a captain, sending the next player to the field, choosing a bowler, and managing the batting order.
 3. `players` : Represents the file where object of player type object using the `Player` class. with attributes such as name, bowling, batting, fielding, running, and experience.
 4. `umpire` : For the handling of score of each match and predicting the outcome of each ball based on the conditions provided and player stats. It has following methods simulate_ball, make_decision,end_innings.
 5. `commentators` : Provides commentary for each ball and over, generating descriptions of game events.
 6. `field` : This file is used to setup tournament with different conditions which are used for predicting ball outcome
 7. `match` : Simulates an individual cricket match, using objects of the above classes to start match, and end the match.
 8. `player_data` : This file is where all the player data is provided which is used for predicting outcomes, players are assigned to their respective teams. you can eaily customize this data using the format specified within the file

## Usage
1. Clone the repository
```
    git clone 
```
2. Navigate to the project directory
```
    cd CricketTournament
```
3. Run the `main.py` file to start the simulation
```
    python main.py
```


