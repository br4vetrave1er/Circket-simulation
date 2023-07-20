class Player:
    '''Player class'''
    def __init__(
            self, name, 
            batting_stats, 
            bowling_stats, 
            fielding_stats, 
            running_stats, 
            experience):
        self.name = name
        self.batting_stats = batting_stats
        self.bowling_stats = bowling_stats
        self.fielding_stats = fielding_stats
        self.running_stats = running_stats
        self.experience = experience

    def calculate_score(self):
        '''Overall score of based on player stats used for prediction'''
        score = self.batting_stats * self.experience + self.running_stats
        return score
