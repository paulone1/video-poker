import random
import datetime
import time


class Cards:
    """This class represents cards."""

    def __init__(self):
        super().__init__()
        self.deck = [
            "clubs_2",
            "clubs_3",
            "clubs_4",
            "clubs_5",
            "clubs_6",
            "clubs_7",
            "clubs_8",
            "clubs_9",
            "clubs_10",
            "clubs_jack",
            "clubs_queen",
            "clubs_king",
            "clubs_ace",
            "diamonds_2",
            "diamonds_3",
            "diamonds_4",
            "diamonds_5",
            "diamonds_6",
            "diamonds_7",
            "diamonds_8",
            "diamonds_9",
            "diamonds_10",
            "diamonds_jack",
            "diamonds_queen",
            "diamonds_king",
            "diamonds_ace",
            "hearts_2",
            "hearts_3",
            "hearts_4",
            "hearts_5",
            "hearts_6",
            "hearts_7",
            "hearts_8",
            "hearts_9",
            "hearts_10",
            "hearts_jack",
            "hearts_queen",
            "hearts_king",
            "hearts_ace",
            "spades_2",
            "spades_3",
            "spades_4",
            "spades_5",
            "spades_6",
            "spades_7",
            "spades_8",
            "spades_9",
            "spades_10",
            "spades_jack",
            "spades_queen",
            "spades_king",
            "spades_ace",
        ]

    def ten_card_deck(self):  # Creates the ten cards needed for the game
        self.ten_cards = random.sample(self.deck, 10)
        return self.ten_cards


def calc_win(cards_to_check, bet):
    winning_words = ""
    wins = 0
    card_numbers_list = []  #  Used for just list of card numbers
    card_suits = []  #  Used for card suits only
    cards_to_check_norm = []  #  Used to normalise list of cards ace = 14 etc
    for card in cards_to_check:
        split_str = card.split("_")
        if split_str[1] == "ace":
            card_suit_number = split_str[0] + "_14"
            cards_to_check_norm.append(card_suit_number)
            card_numbers_list.append(14)
            card_suits.append(split_str[0])
        elif split_str[1] == "king":
            card_suit_number = split_str[0] + "_13"
            cards_to_check_norm.append(card_suit_number)
            card_numbers_list.append(13)
            card_suits.append(split_str[0])
        elif split_str[1] == "queen":
            card_suit_number = split_str[0] + "_12"
            cards_to_check_norm.append(card_suit_number)
            card_numbers_list.append(12)
            card_suits.append(split_str[0])
        elif split_str[1] == "jack":
            card_suit_number = split_str[0] + "_11"
            cards_to_check_norm.append(card_suit_number)
            card_numbers_list.append(11)
            card_suits.append(split_str[0])
        else:
            card_suit_number = split_str[0] + "_" + split_str[1]
            cards_to_check_norm.append(card_suit_number)
            card_numbers_list.append(int(split_str[1]))
            card_suits.append(split_str[0])
    count_duplicates = {i: card_numbers_list.count(i) for i in card_numbers_list}
    count_duplicates_suits = {i: card_suits.count(i) for i in card_suits}
    card_numbers_list.sort()
    # Check royal flush need to check suits
    if winning_words == "":
        for i in count_duplicates_suits:
            if count_duplicates_suits[i] == 5:
                # create list of card numbers that match the suit
                check_royal_list_flush_cards = []
                for s in cards_to_check_norm:
                    split_card = s.split("_")
                    if split_card[0] == i:
                        check_royal_list_flush_cards.append(int(split_card[1]))
                check_royal_list_flush_cards.sort()
                if (
                    check_royal_list_flush_cards[0] + 4
                    == check_royal_list_flush_cards[4]
                    and check_royal_list_flush_cards[0] == 10
                ):
                    winning_words = "Royal flush"
                    wins = bet * 250
    # check_straight_flush
    if winning_words == "":
        for j in count_duplicates_suits:
            if count_duplicates_suits[j] == 5:
                # create list of card numbers that match the suit
                check_straight_list_flush_cards = []
                for k in cards_to_check_norm:
                    split_card = k.split("_")
                    if split_card[0] == j:
                        check_straight_list_flush_cards.append(int(split_card[1]))
                check_straight_list_flush_cards.sort()
                if (
                    check_straight_list_flush_cards[0] + 4
                    == check_straight_list_flush_cards[4]
                ):
                    winning_words = "Straight flush"
                    wins = bet * 50
    # check_four_of_a_kind
    if winning_words == "":
        for l in count_duplicates:
            if count_duplicates[l] == 4:
                winning_words = "Four of a kind"
                wins = bet * 25
    # check full house
    check_full_house = []
    if winning_words == "":
        for m in count_duplicates:
            if count_duplicates[m] == 2:
                check_full_house.append(2)
            if count_duplicates[m] == 3:
                check_full_house.append(3)
        check_full_house.sort(reverse=True)
        if len(check_full_house) > 2:
            if check_full_house[0] == 3 and check_full_house[1] == 2:
                winning_words = "Full house"
                wins = bet * 9
    # check_flush
    if winning_words == "":
        for n in count_duplicates_suits:
            if count_duplicates_suits[n] == 5:
                winning_words = "Flush"
                wins = bet * 6
    # check straight
    check_straight_list = []
    check_straight = 0
    if winning_words == "":
        for o in card_numbers_list:
            if check_straight + 1 == o:
                check_straight = o
                check_straight_list.append(1)
                if len(check_straight_list) == 5:
                    winning_words = "Straight"
                    wins = bet * 4
            else:
                check_straight = o
    # check_three_of_a_kind
    if winning_words == "":
        for p in count_duplicates:
            if count_duplicates[p] == 3:
                winning_words = "Three of a kind"
                wins = bet * 3
    # check 2 pairs
    check_two_pairs = []
    if winning_words == "":
        for q in count_duplicates:
            if count_duplicates[q] == 2:
                check_two_pairs.append(2)
        check_two_pairs.sort()
        if len(check_two_pairs) > 2:
            if check_two_pairs[0] == 2 and check_two_pairs[1] == 2:
                winning_words = "Two pair"
                wins = bet * 2
    # check_jacks_pairs
    if winning_words == "":
        for r in count_duplicates:
            if count_duplicates[r] == 2 and r >= 11:
                if r == 14:
                    y = "Ace"
                elif r == 13:
                    y = "King"
                elif r == 12:
                    y = "Queen"
                elif r == 11:
                    y = "Jack"
                winning_words = f"Pair {y}'s"
                wins = bet
    return winning_words, wins


def game_engine(ten_cards):
    credit = 25
    bet = 0
    wins = 0
    first_five_cards = ten_cards[:5]
    print(f"first five cards: {first_five_cards}")
    held_cards = input(
        "Which card(s) to hold [1-5], 0 for none, space between numbers "
    )
    cards_played = []
    held_card_number_list = held_cards.split()
    first_item = held_card_number_list[0]
    if int(first_item) > 0:
        for i in held_card_number_list:
            card_index = int(i) - 1
            held_card = first_five_cards[card_index]
            cards_played.append(held_card)
    print(f"cards held: {cards_played}")
    number_cards_needed = 5 - len(cards_played)
    if number_cards_needed > 0:
        for j in range(number_cards_needed):
            new_card_index = 5 + j
            new_card = ten_cards[new_card_index]
            cards_played.append(new_card)
    print(f"cards played: {cards_played}")
    bet = 1
    winning_words, winnings = calc_win(cards_played, bet)
    print(winning_words)
    log_file(ten_cards, cards_played, winnings, winning_words)  #  Write to log file
    time.sleep(3)
    main()
    print("END of GAME")


def log_file(ten_cards, cards_played, winnings, winning_words):
    with open("video_poker_log.txt", "a") as f:
        output_list = []
        date_time = datetime.datetime.now()
        date_time_string = date_time.strftime("%m/%d/%Y, %H:%M:%S")
        wins_string = str(winnings)
        ten_cards_string = str(ten_cards)
        cards_played_string = str(cards_played)
        output_list.append(date_time_string)
        output_list.append(wins_string)
        output_list.append(winning_words)
        output_list.append(cards_played_string)
        output_list.append(ten_cards_string)
        win_potential_text, potential_winnings = calc_win(
            ten_cards,
            1,
        )
        win_potential = str(potential_winnings)
        output_list.append(win_potential)
        output_list.append(win_potential_text)
        output = ",".join(output_list)
        f.write(output)
        f.write("\n")


def main():
    run = True
    ins_cards = Cards()  #  Creates the instance of the Card class
    ten_cards = ins_cards.ten_card_deck()  #  create the ten cards for the game

    while run:
        game_engine(ten_cards)


if __name__ == "__main__":  # Call the main function, start up the game
    main()
