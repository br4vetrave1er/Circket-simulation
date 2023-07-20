import random

class Field:
    '''Field class for used for simulation'''
    def __init__(self):
        self.random_data_select()

    def calculate_boundary_probability(self, fielding_stats):
        '''Boundary probability prediction based on conditions and fielding stats'''
        if self.pitch_conditions == "Dry":
            return 0.2 + fielding_stats * 0.05
        elif self.pitch_conditions == "Dusty":
            return 0.3 + fielding_stats * 0.05
        elif self.pitch_conditions == "Green":
            return 0.1 + fielding_stats * 0.05
        else:
            return 0.2 + fielding_stats * 0.05

    def calculate_run_probability(self, fielding_stats):
        '''Runs probability prediction based on conditions and fielding stats'''
        if self.pitch_conditions == "Dry":
            return 0.7 - fielding_stats * 0.05
        elif self.pitch_conditions == "Dusty":
            return 0.6 - fielding_stats * 0.05
        elif self.pitch_conditions == "Green":
            return 0.8 - fielding_stats * 0.05
        else:
            return 0.7 - fielding_stats * 0.05

    def random_data_select(self):
        '''Method for random selecton of field conditions'''
        self.name = random.choice(['Feild1','Feild2','Feild3','Feild4','Feild5','Feild6','Feild7','Feild8','Feild9','Feild10','Feild11' ])
        self.size = random.randint(1000,50000)
        self.fan_ratio = random.randint(0,10**2)/10**2
        self.pitch_conditions = random.choice(['Dry', 'Green', 'Dusty'])