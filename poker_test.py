import poker_engine

# test logic

cards_played_dict = {"cards_played_royal_flush":["spades_10", "spades_jack", "spades_queen", "spades_king", "spades_ace",],
                    "cards_played_straight_flush":["hearts_5", "hearts_6", "hearts_7", "hearts_8", "hearts_9"],
                    "cards_played_four_kind":["hearts_2", "spades_2", "diamonds_2", "clubs_2", "clubs_ace"],
                    "cards_played_full_house":["clubs_queen", "diamonds_queen", "hearts_2", "spades_2", "diamonds_2"],
                    "cards_played_flush":["hearts_6", "hearts_2", "hearts_queen", "hearts_8", "hearts_9"],
                    "cards_played_straight":["hearts_5", "spades_6", "diamonds_7", "clubs_8", "hearts_9"],
                    "cards_played_three_kind":["hearts_2", "spades_2", "diamonds_2","hearts_8", "hearts_9"],
                    "cards_played_two_pairs":["hearts_2", "spades_2", "clubs_queen", "diamonds_queen", "clubs_ace"],
                    "cards_played_pair":["hearts_queen", "hearts_6","spades_queen","spades_2","hearts_8"],
                    "none":["hearts_queen", "hearts_8", "spades_2", "diamonds_7","diamonds_2"]}


ten_cards_played_dict = {"cards_played_royal_flush":["spades_10", "spades_jack", "spades_queen", "spades_king", "spades_ace",],
                    "cards_played_straight_flush":["hearts_5", "hearts_6", "hearts_7", "hearts_8", "hearts_9"],
                    "cards_played_four_kind":["hearts_2", "spades_2", "diamonds_2", "clubs_2", "clubs_ace"],
                    "cards_played_full_house":["clubs_queen", "diamonds_queen", "hearts_2", "spades_2", "diamonds_2"],
                    "cards_played_flush":["hearts_6", "hearts_2", "hearts_queen", "hearts_8", "hearts_9"],
                    "cards_played_straight":["hearts_5", "spades_2", "diamonds_ace", "clubs_8", "hearts_9", "hearts_queen", "hearts_8", "spades_2", "diamonds_7","diamonds_6"],
                    "cards_played_three_kind":["hearts_2", "spades_2", "diamonds_2","hearts_8", "hearts_9"],
                    "cards_played_two_pairs":['spades_3', 'clubs_2', 'diamonds_queen', 'hearts_king', 'hearts_5', 'spades_queen', 'spades_8', 'diamonds_2', 'clubs_ace', 'hearts_6'],
                    "cards_played_pair":["hearts_queen", "hearts_6","spades_queen","spades_2","hearts_8"]}

straight = ("hearts_5", "spades_2", "diamonds_ace", "clubs_8", "hearts_9", "hearts_queen", "hearts_8", "spades_2", "diamonds_7","diamonds_6")

engine = poker_engine.Calc_win()

winning_words, wins = engine.calc_win(straight, 1)
print(f"Test: {straight}, winning text: {winning_words}")

#for ten_cards_played in ten_cards_played_dict:
#    if ten_cards_played == "cards_played_straight":
#        winning_words, wins = engine.calc_win(cards_played_dict[ten_cards_played], 1)
#        print(f"Test: {ten_cards_played}, winning text: {winning_words}")

# all test
#for cards_played in cards_played_dict:
#    winning_words, _ = engine.calc_win(cards_played_dict[cards_played], 1)
#    print(f"Test: {cards_played}, winning text: {winning_words}")
#for ten_cards_played in ten_cards_played_dict:
#    ten_winning_words, _ = engine.calc_win(ten_cards_played_dict[ten_cards_played], 1)
#    print(f"Ten Test: {ten_cards_played}, winning text: {ten_winning_words}")
