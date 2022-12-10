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
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}
SHAPE_MAPPINGS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}
OUTCOME_MAPPINGS = {
    'win': 6,
    'draw': 3,
    'loss': 0,
}


def get_shape_one(encoded_input):
    """From encoded input (A,B,C/X,Y,Z), get value of shape used"""

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
        self.outcome_score = OUTCOME_MAPPINGS[outcome]
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
        self.opponent = get_shape_one(self.encoded_opponent)
        self.me = get_shape_one(self.encoded_me)

    def battle(self):
        """Perform RPS battle"""

        outcome = self.get_outcome()
        self.outcome_score = OUTCOME_MAPPINGS[outcome]
        self.shape_score = get_shape_value(self.me)


def get_data():
    """Get data from input"""

    return get_input(FILENAME, 'basic')


def do_battles(data):
    """Do all rock-paper-scissors battles

    :param list<string> data: Data from input
    :returns: Int. Total score from all battles
    """

    total_score = 0
    for entry in data:
        rps = RPS_Battle_One(entry)
        rps.battle()
        rps.calculate_total_score()
        total_score += rps.total_score
    return total_score


def main():
    data = get_data()
    total_score = do_battles(data)
    print_results(total_score, blurb='PART ONE: RPS Score')


if __name__ == '__main__':
    main()
