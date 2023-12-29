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


def _get_highest_count(unique_cards, cards):
    """Helper method to get highest count of each unique card"""
    unique_cards = {k: 0 for k in unique_cards}
    for card in cards:
        unique_cards[card] += 1
    unique_counts = [x for x in list(unique_cards.values())]
    return max(unique_counts)


def get_hand_type(cards: str):
    """From cards, get hand type

    1: Five of a kind, where all five cards have the same label: AAAAA
    2: Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    3: Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    4: Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    5: Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    6: One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    7: High card, where all cards' labels are distinct: 23456
    """
    unique_cards = set(cards)
    if len(unique_cards) == 5:  # High card: 56789
        hand_type = 7
    elif len(unique_cards) == 4:  # One pair: 88AKJ
        hand_type = 6
    elif len(unique_cards) == 3:
        highest_count = _get_highest_count(unique_cards, cards)
        if highest_count == 3:  # Three of a kind: 333T8
            hand_type = 4
        else:  # highest count == 2  Two pair: QQ445
            hand_type = 5
    elif len(unique_cards) == 2:
        highest_count = _get_highest_count(unique_cards, cards)
        if highest_count == 4:  # 4-of-a-kind: 22229
            hand_type = 2
        else:  # highest count == 3  Full house: 77755
            hand_type = 3
    else:  # len(unique_cards) == 1  Five of a kind: JJJJJ
        hand_type = 1
    return hand_type


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
