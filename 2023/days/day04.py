# TITLE: Scratchcards
from utils import get_file_contents, clean_list, convert_str_to_int, plog
import re
INPUT_FILE = 'input/day04.txt'


def get_matching_winning_numbers(your_numbers: list, winning_numbers: list) -> list:
    """Compare two lists and get winning matches

    :param your_numbers: List of your numbers
    :param winning_numbers: List of winning numbers
    :returns: List of matching winning numbers
    """
    return list(set(your_numbers).intersection(set(winning_numbers)))


def calculate_points(winning_numbers: list) -> int:
    """From a list of matching winning numbers, calculate the points"""
    # challenge to self: can you do this without multiplying?
    if not winning_numbers:
        return 0
    if len(winning_numbers) == 1:
        return 1
    points = 1
    for _ in winning_numbers[1:]:
        points += points
    return points


def parse_numbers(line: str) -> (list, list):
    """Parse line and get your numbers / winning numbers"""
    raw_numbers = line.split(':')[1]
    split_numbers = raw_numbers.split('|')
    raw_your_numbers = split_numbers[0]
    raw_winning_numbers = split_numbers[1]

    your_numbers = clean_list(raw_your_numbers.split(' '))
    your_numbers = [convert_str_to_int(x) for x in your_numbers]
    winning_numbers = clean_list(raw_winning_numbers.split(' '))
    winning_numbers = [convert_str_to_int(x) for x in winning_numbers]
    return your_numbers, winning_numbers


def puzzle_one(raw_data: list) -> int:
    """How many points are the scratchcards worth in total?"""
    total = 0
    for line in raw_data:
        your_numbers, winning_numbers = parse_numbers(line)
        matching_numbers = get_matching_winning_numbers(your_numbers, winning_numbers)
        total += calculate_points(matching_numbers)
    return total


def get_card_count(scratchcards: dict, current_cards: list, cards_gained: list) -> list:
    """Recursively get card count for matching winning cards"""
    if not cards_gained:
        return current_cards
    new_cards = []
    for num in cards_gained:
        matching_cards = scratchcards[num]
        if matching_cards:
            for add_num, _ in enumerate(matching_cards, start=1):
                new_card_num = num + add_num
                new_cards.append(new_card_num)
                current_cards.append(new_card_num)
    return get_card_count(scratchcards, current_cards, new_cards)


def puzzle_two(raw_data: list) -> int:
    """How many total scratchcards do you end up with?"""
    scratchcards = {k: {} for k, _ in enumerate(raw_data)}
    current_cards = []
    cards_gained = []
    for index, line in enumerate(raw_data):
        your_numbers, winning_numbers = parse_numbers(line)
        matching_numbers = get_matching_winning_numbers(your_numbers, winning_numbers)
        scratchcards[index] = matching_numbers
        current_cards.append(index)
        if matching_numbers:
            cards_gained.append(index)
    result = get_card_count(scratchcards, current_cards, cards_gained)
    return len(result)


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
