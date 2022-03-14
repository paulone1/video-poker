import pygame
import poker_constants


# ---classes----
class Hold_button:
    """This class represents Hold button.
    It needs the hold button number, and the state.
    State is 0 = off, 1 = on."""

    def __init__(self, number, state):
        super().__init__()
        self.font = pygame.font.SysFont("arial", 25)
        self.image = pygame.Surface([130, 30])
        self.number = number
        self.state = state

    def draw_hold_button(self, SCREEN):
        if self.state == 0:
            self.text_surf = self.font.render("HOLD", 1, poker_constants.BLACK)
            self.image.fill(poker_constants.WHITE)
        if self.state == 1:
            self.text_surf = self.font.render("HOLD", 1, poker_constants.WHITE)
            self.image.fill(poker_constants.AMBER)
        self.rect = self.image.get_rect()
        W = self.text_surf.get_width()
        H = self.text_surf.get_height()
        self.rect.y = 753
        if self.number == 1:
            self.rect.x = 99
            self.image.blit(self.text_surf, [130 / 2 - W / 2, 30 / 2 - H / 2])
            SCREEN.blit(self.image, self.rect)
        if self.number == 2:
            self.rect.x = 338
            self.image.blit(self.text_surf, [130 / 2 - W / 2, 30 / 2 - H / 2])
            SCREEN.blit(self.image, self.rect)
        if self.number == 3:
            self.rect.x = 577
            self.image.blit(self.text_surf, [130 / 2 - W / 2, 30 / 2 - H / 2])
            SCREEN.blit(self.image, self.rect)
        if self.number == 4:
            self.rect.x = 816
            self.image.blit(self.text_surf, [130 / 2 - W / 2, 30 / 2 - H / 2])
            SCREEN.blit(self.image, self.rect)
        if self.number == 5:
            self.rect.x = 1055
            self.image.blit(self.text_surf, [130 / 2 - W / 2, 30 / 2 - H / 2])
            SCREEN.blit(self.image, self.rect)


class Deal_button:
    """This class represents Deal button."""

    def __init__(self, bet):
        super().__init__()
        self.font = pygame.font.SysFont("arial", 25)
        text_colour = poker_constants.BLACK
        button_colour = poker_constants.GREY
        if bet >= 1:
            button_colour = poker_constants.WHITE
        self.text_surf = self.font.render("DEAL", 1, text_colour)
        self.image = pygame.Surface([200, 50])
        self.image.fill(button_colour)
        self.rect = self.image.get_rect()
        self.rect.x = poker_constants.WIDTH // 2 - 100
        self.rect.y = 850
        W = self.text_surf.get_width()
        H = self.text_surf.get_height()
        self.image.blit(self.text_surf, [200 / 2 - W / 2, 50 / 2 - H / 2])

    def draw_deal_button(self, SCREEN):
        SCREEN.blit(self.image, self.rect)


class Bet_button:
    """This class represents Bet button."""

    def __init__(self, bet, state):
        super().__init__()
        self.font = pygame.font.SysFont("arial", 25)
        text_colour = poker_constants.BLACK
        button_colour = poker_constants.WHITE
        if bet == 5 or state == 1:
            button_colour = poker_constants.GREY
        self.text_surf = self.font.render("BET £1", 1, text_colour)
        self.image = pygame.Surface([130, 30])
        self.image.fill(button_colour)
        self.rect = self.image.get_rect()
        self.rect.x = 930
        self.rect.y = 860
        W = self.text_surf.get_width()
        H = self.text_surf.get_height()
        self.image.blit(self.text_surf, [130 / 2 - W / 2, 30 / 2 - H / 2])

    def draw_bet_button(self, SCREEN):
        SCREEN.blit(self.image, self.rect)


class Max_button:
    """This class represents a button."""

    def __init__(self, bet, state):
        super().__init__()
        text_colour = poker_constants.BLACK
        button_colour = poker_constants.WHITE
        if bet == 5 or state == 1:
            button_colour = poker_constants.GREY
        self.font = pygame.font.SysFont("arial", 25)
        self.text_surf = self.font.render("MAX BET", 1, text_colour)
        self.image = pygame.Surface([130, 30])
        self.image.fill(button_colour)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 860
        W = self.text_surf.get_width()
        H = self.text_surf.get_height()
        self.image.blit(self.text_surf, [130 / 2 - W / 2, 30 / 2 - H / 2])

    def draw_max_button(self, SCREEN):
        SCREEN.blit(self.image, self.rect)
