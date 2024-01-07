# TITLE: Camel Cards
from utils import get_file_contents, plog
import re


INPUT_FILE = 'input/day07.txt'
LETTER_MAP = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def _get_unique_count(cards):
    """Helper method to get unique count of each card"""
    unique_cards = set(cards)
    unique_cards = {k: 0 for k in unique_cards}
    for card in cards:
        unique_cards[card] += 1
    return unique_cards


def _get_highest_count(cards):
    """Helper method to get highest count of each unique card"""
    unique_cards = _get_unique_count(cards)
    unique_counts = [x for x in list(unique_cards.values())]
    return max(unique_counts)


def _convert_jokers(cards: str) -> str:
    """From cards, convert joker to best card"""
    unique_counts = _get_unique_count(cards)
    max_key = None
    max_count = 0
    for key, count in unique_counts.items():
        if count > max_count and key != 'J':
            max_count = count
            max_key = key
    if not max_key:  # implies the card set is JJJJJ
        return cards
    return cards.replace('J', max_key)


def get_hand_type(cards: str, use_joker=False):
    """From cards, get hand type. Weakest hand type will have lowest rank"""
    if use_joker:
        cards = _convert_jokers(cards)
    unique_cards = set(cards)
    if len(unique_cards) == 5:  # High card: 56789
        hand_type = 1
    elif len(unique_cards) == 4:  # One pair: 88AKJ
        hand_type = 2
    elif len(unique_cards) == 3:
        highest_count = _get_highest_count(cards)
        if highest_count == 3:  # Three of a kind: 333T8
            hand_type = 4
        else:  # highest count == 2  Two pair: QQ445
            hand_type = 3
    elif len(unique_cards) == 2:
        highest_count = _get_highest_count(cards)
        if highest_count == 4:  # Four of a kind: 22229
            hand_type = 6
        else:  # highest count == 3  Full house: 77755
            hand_type = 5
    else:  # len(unique_cards) == 1  Five of a kind: JJJJJ
        hand_type = 7
    return hand_type


def _convert_letter(char: str, use_joker=False):
    try:
        int_repr = int(char)
    except ValueError:
        int_repr = LETTER_MAP.get(char)
        if use_joker and int_repr == 11:  # J is now Joker which has a lower value
            int_repr = -1
    return int_repr


def compare_cards(hand_one: str, hand_two: str, use_joker=False):
    """Compare each individual card in hand return stronger hand"""
    stronger_hand = None
    for index in range(5):
        hand_one_char = _convert_letter(hand_one[index], use_joker=use_joker)
        hand_two_char = _convert_letter(hand_two[index], use_joker=use_joker)
        if hand_one_char == hand_two_char:
            continue
        if hand_one_char > hand_two_char:
            stronger_hand = hand_one
        else:
            stronger_hand = hand_two
        break
    return stronger_hand


def compare_hands(hand_one: str, hand_two: str, use_joker=False):
    """Compare hands and return the stronger hand"""
    stronger_hand = None
    hand_one_rank = get_hand_type(hand_one, use_joker=use_joker)
    hand_two_rank = get_hand_type(hand_two, use_joker=use_joker)
    if hand_one_rank == hand_two_rank:
        stronger_hand = compare_cards(hand_one, hand_two, use_joker=use_joker)
    elif hand_one_rank > hand_two_rank:
        stronger_hand = hand_one
    else:
        stronger_hand = hand_two
    return stronger_hand


def _quick_sort(arr, use_joker=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if compare_hands(x, pivot, use_joker=use_joker) == pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if compare_hands(x, pivot, use_joker=use_joker) == x]
    return _quick_sort(left, use_joker=use_joker) + middle + _quick_sort(right, use_joker=use_joker)


def puzzle_one(raw_data: list, use_joker=False) -> int:
    """What are the total winnings?"""
    bid_map = {}
    hands = []
    for row in raw_data:
        hand, bid = row.split(' ')
        hands.append(hand)
        bid_map[hand] = int(bid)
    sorted_hands = _quick_sort(hands, use_joker=use_joker)
    total = 0
    for rank, hand in enumerate(sorted_hands, start=1):
        total += rank * bid_map.get(hand)
    return total


def puzzle_two(raw_data: list) -> int:
    """Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?"""
    return puzzle_one(raw_data, use_joker=True)


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
