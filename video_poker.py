import pygame
import time
import poker_constants
import poker_card
import poker_buttons
import poker_win_table
import poker_engine


class Game(object):
    def __init__(self):
        self.back_image_file = "./assets/red2.png"
        self.deal_state = 0
        self.hold_buttons_states = {
            "button1_state": 0,
            "button2_state": 0,
            "button3_state": 0,
            "button4_state": 0,
            "button5_state": 0,
        }
        self.cards_played=[]
        self.font = pygame.font.SysFont("arial", 25)
        self.bold_font = pygame.font.SysFont("arial", 25, bold=True)
        self.winning_font = pygame.font.Font("./fonts/CoffeeTin.ttf", 100)
        self.credit = 25
        self.bet = 0
        self.wins = 0
        self.winning_words = ""
        self.card = poker_card.Card()                       # Creates instance of class saves writing poker_card.Card every time
        self.engine_deal_cards = poker_engine.Deal_cards()  # Creates instance of class saves writing poker_engine.Deal_cards every time
        self.engine_calc_win = poker_engine.Calc_win()      # Creates instance of class saves writing poker_engine.Calc_win every time
        self.ten_cards = self.card.ten_card_deck()          # Calls function to create ten cards may to move if its too fixed        
        self.deal_sound = pygame.mixer.Sound("./sounds/deal.mp3")
        self.win_sound = pygame.mixer.Sound("./sounds/wins.wav")
        self.loose_sound = pygame.mixer.Sound("./sounds/loose.wav")
        self.credit_sound = pygame.mixer.Sound("./sounds/credit.wav")
        self.bet_sound = pygame.mixer.Sound("./sounds/bet.wav")

    def process_events(self):
        """Process all of the events. Return a "True" if we need
        to close the window."""
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.deal_button.rect.collidepoint(pos) and self.bet > 0:
                        if self.deal_state == 0:
                            self.deal_state = 1
                            pygame.mixer.Sound.play(self.deal_sound)
                        else:
                            self.deal_state = 2
                            pygame.mixer.Sound.play(self.deal_sound)
                            self.winning_words, self.wins, self.cards_played, self.credit =(
                                self.engine_calc_win.finish_game(
                                self.ten_cards, self.hold_buttons_states, self.bet, self.credit))
                            if self.wins > 0:
                                pygame.mixer.Sound.play(self.win_sound)
                            elif self.wins == 0:
                                  pygame.mixer.Sound.play(self.loose_sound)
                            elif self.credit == 0:
                                pygame.mixer.Sound.play(self.credit_sound)
                    if self.bet_button.rect.collidepoint(pos) and self.credit >= 1:
                        if self.deal_state == 0 and self.bet < 5:
                            self.bet += 1
                            self.credit -= 1
                            pygame.mixer.Sound.play(self.bet_sound)
                    if self.max_button.rect.collidepoint(pos) and self.credit >= 5:
                        if self.deal_state == 0 and self.bet < 5:
                            self.bet = 5
                            self.credit -= 5
                            pygame.mixer.Sound.play(self.bet_sound)
                    if self.hold_button1.rect.collidepoint(pos):
                        if self.hold_buttons_states["button1_state"] == 0:
                            self.hold_buttons_states["button1_state"] = 1
                        else:
                            self.hold_buttons_states["button1_state"] = 0
                    if self.hold_button2.rect.collidepoint(pos):
                        if self.hold_buttons_states["button2_state"] == 0:
                            self.hold_buttons_states["button2_state"] = 1
                        else:
                            self.hold_buttons_states["button2_state"] = 0
                    if self.hold_button3.rect.collidepoint(pos):
                        if self.hold_buttons_states["button3_state"] == 0:
                            self.hold_buttons_states["button3_state"] = 1
                        else:
                            self.hold_buttons_states["button3_state"] = 0
                    if self.hold_button4.rect.collidepoint(pos):
                        if self.hold_buttons_states["button4_state"] == 0:
                            self.hold_buttons_states["button4_state"] = 1
                        else:
                            self.hold_buttons_states["button4_state"] = 0
                    if self.hold_button5.rect.collidepoint(pos):
                        if self.hold_buttons_states["button5_state"] == 0:
                            self.hold_buttons_states["button5_state"] = 1
                        else:
                            self.hold_buttons_states["button5_state"] = 0
        return True


    def display_frame(self, SCREEN):
        """Display everything to the screen for the game."""
        SCREEN.fill(poker_constants.BLUE)
        
        if self.deal_state == 0:
            self.card.card_draw_back(self.back_image_file, SCREEN)  # Draw back of card

        if self.deal_state == 1:
            self.engine_deal_cards.deal(self.ten_cards, SCREEN) # Draw front of cards for 1st time

        if self.deal_state == 2:
            self.engine_deal_cards.deal(self.cards_played, SCREEN)
            
        self.deal_button = poker_buttons.Deal_button(self.bet)
        self.max_button = poker_buttons.Max_button(self.bet, self.deal_state)
        self.bet_button = poker_buttons.Bet_button(self.bet, self.deal_state)

        self.deal_button.draw_deal_button(SCREEN)
        self.max_button.draw_max_button(SCREEN)
        self.bet_button.draw_bet_button(SCREEN)        
        
        self.hold_button1 = poker_buttons.Hold_button(1, self.hold_buttons_states["button1_state"])
        self.hold_button2 = poker_buttons.Hold_button(2, self.hold_buttons_states["button2_state"])
        self.hold_button3 = poker_buttons.Hold_button(3, self.hold_buttons_states["button3_state"])
        self.hold_button4 = poker_buttons.Hold_button(4, self.hold_buttons_states["button4_state"])
        self.hold_button5 = poker_buttons.Hold_button(5, self.hold_buttons_states["button5_state"])             
        self.hold_button1.draw_hold_button(SCREEN)
        self.hold_button2.draw_hold_button(SCREEN)
        self.hold_button3.draw_hold_button(SCREEN)
        self.hold_button4.draw_hold_button(SCREEN)
        self.hold_button5.draw_hold_button(SCREEN)
        
        self.win_table = poker_win_table.Win_table(self.bet)  
        self.win_table.draw_win_table(SCREEN)
        
        self.money_text = self.font.render(
            f"Credit: £{self.credit}", True, poker_constants.WHITE
        )
        self.bet_text = self.font.render(
            f"Bet: £{self.bet}", True, poker_constants.WHITE
        )
        self.wins_text = self.bold_font.render(
            f"Wins: £{self.wins}", True, poker_constants.YELLOW
        )
        self.winning_text = self.winning_font.render(
            f"{self.winning_words}", True, poker_constants.YELLOW
        )
        SCREEN.blit(self.money_text, (89, 350))
        SCREEN.blit(self.bet_text, (89, 400))
        if self.wins > 0:
            SCREEN.blit(self.wins_text, (89, 450))
            SCREEN.blit(
                self.winning_text,
                (poker_constants.WIDTH // 2 - self.winning_text.get_width() // 2, 350),
            )
        
        pygame.display.flip()
    
    def restart(self):
        if self.deal_state == 2:
            time.sleep(3)
            if self.credit == 0:
                self.credit = 25
            self.deal_state = 0
            self.hold_buttons_states = {
                "button1_state": 0,
                "button2_state": 0,
                "button3_state": 0,
                "button4_state": 0,
                "button5_state": 0,
            }
            self.cards_played=[]
            self.bet = 0
            self.wins = 0
            self.winning_words = ""
            self.ten_cards = self.card.ten_card_deck()


def main():
    """Main program function."""
    pygame.init()  # Initialize Pygame and set up the window
    pygame.mixer.init()  # Initialize Pygame sounds

    SIZE = [poker_constants.WIDTH, poker_constants.HEIGHT]
    SCREEN = pygame.display.set_mode(SIZE)

    pygame.display.set_caption("Video poker")

    run = True  # Create our objects and set the data
    clock = pygame.time.Clock()

    game = Game()  # Create an instance of the Game class

    while run:  # Main game loop
        run = game.process_events()  # Process events (keystrokes, mouse clicks, etc)
        game.display_frame(SCREEN)  # Draw the current frame
        game.restart()  # restart game
        clock.tick(10)  # Pause for the next frame

    pygame.quit()  # Close window and exit


if __name__ == "__main__":  # Call the main function, start up the game
    main()
