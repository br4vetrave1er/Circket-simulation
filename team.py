class Team:
    def __init__(
            self, name, 
            players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []
        self.bowling_order = []

    def select_captain(
            self, 
            captain):
        '''Selection of captain'''
        self.captain = captain

    def send_next_player(self):
        '''Next player in the batting order'''
        if not self.batting_order:
            self.decide_batting_order()
        return self.batting_order.pop(0)

    def choose_bowler(self):
        '''Bowler selection'''
        if not self.bowling_order:
            self.decide_bowling_order()
        return self.bowling_order.pop(0)

    def decide_batting_order(self):
        '''Batting order selection'''
        self.batting_order = sorted(
            self.players, 
            key=lambda player: player.batting_stats, 
            reverse=True)

    def decide_bowling_order(self):
        '''Bowling order selection'''
        self.bowling_order = sorted(
            self.players, 
            key=lambda player: player.bowling_stats, 
            reverse=True)

    def add_player(self, player):
        '''Custom player addition to squad'''
        self.players.append(player)

    def remove_player(self, player):
        '''Player removal from squad'''
        self.players.remove(player)
        if player in self.batting_order:
            self.batting_order.remove(player)
        if player in self.bowling_order:
            self.bowling_order.remove(player)


