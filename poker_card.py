import pygame
import random


class Card:
    """class for playing cards"""

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

    def card_draw_back(self, card_image_file, SCREEN):
        """Draws the back of the cards"""
        card_x = 89
        card_y = 500
        for card in range(5):
            self.back_card_image = pygame.image.load(card_image_file).convert_alpha()
            self.back_card_image = pygame.transform.scale(
                self.back_card_image, (150, 213)
            )
            self.back_card_rect = self.back_card_image.get_rect()
            self.back_card_rect.x = card_x
            self.back_card_rect.y = card_y
            SCREEN.blit(self.back_card_image, self.back_card_rect)
            card_x += 239

    def card_draw_front(self, card_image_file, card_x_pos, card_y_pos, SCREEN):   # This function called from poker_engine
        """Draws the front of the card"""
        self.front_card_image = pygame.image.load(card_image_file).convert_alpha()
        self.front_card_image = pygame.transform.scale(
            self.front_card_image, (150, 213)
        )
        self.front_card_rect = self.front_card_image.get_rect()
        self.front_card_rect.x = card_x_pos
        self.front_card_rect.y = card_y_pos
        SCREEN.blit(self.front_card_image, self.front_card_rect)
