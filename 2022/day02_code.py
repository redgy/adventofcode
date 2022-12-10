from utils import get_input
from utils import print_results

FILENAME = 'day02_input_sample.txt'
FILENAME = 'day02_input.txt'
ENCODED_MAPPINGS = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
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


def get_shape_value(encoded_input):
    """From encoded input (A,B,C/X,Y,Z), get value of shape used"""

    return SHAPE_MAPPINGS[ENCODED_MAPPINGS[encoded_input]]


class RPS_Battle:
    """Rock-paper-scissors battle class"""

    def __init__(self, battle_input):
        """Constructor

        :param tuple battle_input: From input, "Opponent You" choices
        """

        self.opponent, self.me = battle_input.split(' ')
        self.score = 0
        self.battle()

    def get_outcome(self):
        """Get outcome of RPS battle

        :returns: Int. Value based off of outcome (see OUTCOME_MAPPINGS)
        """

        if self.opponent == self.me:
            return 'draw'
        if self.me == 'rock':
            if self.opponent == 'paper':
                return 'loss'
            return 'win'
        opponent_shape_value = get_shape_value(self.opponent)
        my_shape_value = get_shape_value(self.me)
        match my_shape_value - opponent_shape_value:
            case -1:
                outcome = 'loss'
            case 1:
                outcome = 'win'
            case _:
                outcome = 'draw'
        return outcome

    def battle(self):
        """Perform RPS battle"""

        outcome = self.get_outcome()
        self.score += OUTCOME_MAPPINGS[outcome]
        self.score += get_shape_value(self.me)


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
        rps = RPS_Battle(entry)
        total_score += rps.score
    print_results(total_score, blurb='PART ONE: RPS Score')


def main():
    data = get_data()
    do_battles(data)


if __name__ == '__main__':
    main()
