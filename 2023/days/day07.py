# TITLE: Camel Cards
from utils import get_file_contents, clean_list, plog
import re
INPUT_FILE = 'input/day07.txt'
LETTER_MAP = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def get_hand_type(cards: str):
    """From cards, get hand type

    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456
    """
    pass


def _convert_letter(char: str):
    try:
        int_repr = int(char)
    except ValueError:
        int_repr = LETTER_MAP.get(char)
    return int_repr


def compare_hands(hand_one: str, hand_two: str):
    for index in range(5):
        hand_one_char = _convert_letter(hand_one[index])
        hand_two_char = _convert_letter(hand_two[index])
        if hand_one_char == hand_two_char:
            continue
        if hand_one_char > hand_two_char:
            return hand_one
        return hand_two
    raise ValueError('both hands are the same')


def puzzle_one(raw_data: list) -> int:
    """What are the total winnings?"""
    pass


def puzzle_two(raw_data: list) -> int:
    """TODO"""
    pass


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
