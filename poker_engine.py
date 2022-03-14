import pygame
import datetime
import os
import poker_card


class Deal_cards:
    def __init__(self):
        pass

    def deal(self, ten_cards, SCREEN):
        first_five_cards = ten_cards[:5]
        card_x_pos = 89
        card_y_pos = 500
        for card in first_five_cards:
            card_image_file = "./assets/" + card + ".png"
            poker_card.Card.card_draw_front(self, card_image_file, card_x_pos, card_y_pos, SCREEN)
            card_x_pos += 239
        

class Calc_win:
    def __init__(self):
        pass


    def finish_game(self, ten_cards, hold_buttons_states, bet, credit):  #  This draws final cards, write log file, pauses game, reset bet, set deal_state to 0 & set hold buttons state to 0
        cards_played = []
        new_card_index = 5
        for i in hold_buttons_states:
            if i == "button1_state":
                if hold_buttons_states[i] == 1:
                    card_index = 0
                    held_card = ten_cards[card_index]
                    cards_played.append(held_card)
                elif hold_buttons_states[i] == 0:
                    new_card = ten_cards[new_card_index]
                    new_card_index += 1
                    cards_played.append(new_card)
            if i == "button2_state":                
                if hold_buttons_states[i] == 1:
                    card_index = 1
                    held_card = ten_cards[card_index]
                    cards_played.append(held_card)
                elif hold_buttons_states[i] == 0:
                    new_card = ten_cards[new_card_index]
                    new_card_index += 1
                    cards_played.append(new_card)
            if i == "button3_state":
                if hold_buttons_states[i] == 1:
                    card_index = 2
                    held_card = ten_cards[card_index]
                    cards_played.append(held_card)
                elif hold_buttons_states[i] == 0:
                    new_card = ten_cards[new_card_index]
                    new_card_index += 1
                    cards_played.append(new_card)
            if i == "button4_state":
                if hold_buttons_states[i] == 1:
                    card_index = 3
                    held_card = ten_cards[card_index]
                    cards_played.append(held_card)
                elif hold_buttons_states[i] == 0:
                    new_card = ten_cards[new_card_index]
                    new_card_index += 1
                    cards_played.append(new_card)
            if i == "button5_state":
                if hold_buttons_states[i] == 1:
                    card_index = 4
                    held_card = ten_cards[card_index]
                    cards_played.append(held_card)
                elif hold_buttons_states[i] == 0:
                    new_card = ten_cards[new_card_index]
                    new_card_index += 1
                    cards_played.append(new_card)
        winning_words, winnings = Calc_win.calc_win(self, cards_played, bet)
        credit += winnings
        Log_file.write_log_file(self, ten_cards, cards_played, winnings, winning_words, bet)
        return winning_words, winnings, cards_played, credit

    def calc_win(self, cards_to_check, bet):        #  calculates win 
        winning_words = ""
        wins = 0
        card_numbers_list = []      #  Used for just list of card numbers
        card_suits = []             #  Used for card suits only
        cards_to_check_norm = []    #  Used to normalise list of cards ace = 14 etc
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
                        if bet == 5:
                            wins = 4000
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
            if len(check_full_house) >= 2:
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
        previous_number = card_numbers_list[0]
        if winning_words == "":
            for o in card_numbers_list:
                if previous_number + 1 == o:
                    check_straight_list.append(o)
                    if len(check_straight_list) == 4:
                        winning_words = "Straight"
                        wins = bet * 4
                previous_number = o
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
            if len(check_two_pairs) >= 2:
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


class Log_file():
    def __init__(self):
        self.date_time = datetime.datetime.now()
        self.date_time_string = self.date_time.strftime("%m/%d/%Y, %H:%M:%S")

    def create_log_file(self):
        with open("video_poker_log.txt", "w") as f:
            output_list = [
                "Date_time",
                "Bet",
                "Win",
                "Winning_text",
                "Cards_played",
                "Potential_win",
                "Potential_winning_text",
                "Ten_cards",
            ]
            output = "|".join(output_list)
            f.write(output)
            f.write("\n")
            return

    def write_log_file(self, ten_cards, cards_played, winnings, winning_words, bet):
        if not os.path.exists("video_poker_log.txt"):
            Log_file.create_log_file(self)

        with open("video_poker_log.txt", "a") as f:
            output_list = []
            date_time = datetime.datetime.now()
            date_time_string = date_time.strftime("%m/%d/%Y, %H:%M:%S")
            bet_string = str(bet)
            wins_string = str(winnings)
            ten_cards_string = str(ten_cards)
            cards_played_string = str(cards_played)
            output_list.append(date_time_string)
            output_list.append(bet_string)
            output_list.append(wins_string)
            output_list.append(winning_words)
            output_list.append(cards_played_string)
            win_potential_text, potential_winnings = Calc_win.calc_win(self, ten_cards, bet)
            win_potential = str(potential_winnings)
            output_list.append(win_potential)
            output_list.append(win_potential_text)
            output_list.append(ten_cards_string)
            output = "|".join(output_list)
            f.write(output)
            f.write("\n")
