from utils import get_input
from utils import print_results

FILENAME = 'day02_input_sample.txt'
FILENAME = 'day02_input.txt'
ENCODED_MAPPINGS_ONE = {  # Part I states encoding is shape
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}
ENCODED_MAPPINGS_TWO = {  # Part II states encoding is outcome
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win',
}
SHAPE_MAPPINGS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}
OUTCOME_MAPPINGS = {
    'win': {
        'score': 6,
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock',
    },
    'draw': {
        'score': 3,
        'rock': 'rock',
        'paper': 'paper',
        'scissors': 'scissors',
    },
    'loss': {
        'score': 0,
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper',
    },
}


def get_shape(encoded_input):
    """PART ONE: from encoded input (A,B,C/X,Y,Z), get value of shape used"""

    return ENCODED_MAPPINGS_ONE[encoded_input]


def get_shape_value(shape):
    """Shape name to value"""

    return SHAPE_MAPPINGS[shape]


class RPS_Battle:
    """Rock-paper-scissors battle class"""

    def __init__(self, battle_input):
        """Constructor

        :param tuple battle_input: From input, "Opponent You" choices
        """

        self.encoded_opponent, self.encoded_me = battle_input.split(' ')
        self.shape_score = 0
        self.outcome_score = 0
        self.total_score = 0

    def get_outcome(self):
        """Get outcome of RPS battle

        :returns: Int. Value based off of outcome (see OUTCOME_MAPPINGS)
        """

        if self.opponent == self.me:
            return 'draw'
        if self.me == 'rock':
            if self.opponent == 'scissors':
                return 'win'
            return 'loss'
        if self.me == 'paper':
            if self.opponent == 'rock':
                return 'win'
            return 'loss'
        if self.me == 'scissors':
            if self.opponent == 'paper':
                return 'win'
            return 'loss'

    def battle(self):
        """Perform RPS battle"""

        outcome = self.get_outcome()
        self.outcome_score = OUTCOME_MAPPINGS[outcome]['score']
        self.shape_score = get_shape_value(self.me)

    def calculate_total_score(self):
        """Calculate total score by adding outcome and shape scores"""

        self.total_score = self.outcome_score + self.shape_score


class RPS_Battle_One(RPS_Battle):
    def __init__(self, battle_input):
        """Constructor for part 1

        :param tuple battle_input: From input, "Opponent You" choices
        """

        super().__init__(battle_input)
        self.opponent = get_shape(self.encoded_opponent)
        self.me = get_shape(self.encoded_me)


class RPS_Battle_Two(RPS_Battle):
    def __init__(self, battle_input):
        """Constructor for part 1

        :param tuple battle_input: From input, "Opponent You" choices
        """

        super().__init__(battle_input)
        self.opponent = get_shape(self.encoded_opponent)
        self.me = self.determine_shape()

    def determine_shape(self):
        outcome = ENCODED_MAPPINGS_TWO[self.encoded_me]
        return OUTCOME_MAPPINGS[outcome][self.opponent]


def get_data():
    """Get data from input"""

    return get_input(FILENAME, 'basic')


def do_battles(data):
    """Do all rock-paper-scissors battles

    :param list<string> data: Data from input
    :returns: Int. Total score from all battles
    """

    total_score_one = 0
    total_score_two = 0
    for entry in data:
        rps = RPS_Battle_One(entry)
        rps.battle()
        rps.calculate_total_score()
        total_score_one += rps.total_score

        rps = RPS_Battle_Two(entry)
        rps.battle()
        rps.calculate_total_score()
        total_score_two += rps.total_score
    return total_score_one, total_score_two


def main():
    data = get_data()
    score1, score2 = do_battles(data)
    print_results(score1, blurb='PART ONE: RPS Score')
    print_results(score2, blurb='PART TWO: RPS Score')


if __name__ == '__main__':
    main()
