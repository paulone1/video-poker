import pygame
import poker_constants

# ---classes----
class Win_table:
    """This class represents text_payout."""

    def __init__(self, bet):
        super().__init__()
        self.payout = (
            [
                ["Stake", "£1", "£2", "£3", "£4", "£5"],
                ["Royal flush", "£250", "£500", "£750", "£1,000", "£4,000"],
                ["Straight flush", "£50", "£100", "£150", "£200", "£250"],
                ["Four of a kind", "£25", "£50", "£75", "£100", "£125"],
                ["Full house", "£9", "£18", "£27", "£36", "£45"],
                ["Flush", "£6", "£12", "£18", "£24", "£30"],
                ["Straight", "£4", "£8", "£12", "£16", "£20"],
                ["Three of a kind", "£3", "£6", "£9", "£12", "£15"],
                ["Two pairs", "£2", "£4", "£6", "£8", "£10"],
                ["Jacks or better", "£1", "£2", "£3", "£4", "£5"],
            ],
        )
        self.bold_font = pygame.font.SysFont("arial", 25, bold=True, italic=False)
        self.bet = bet

    def table_helper(
        self,
        text,
        fill_colour,
        background_width,
        background_height,
        background_x,
        background_y,
        align,
    ):
        """Creates the win text properies"""
        self.text_surf = self.bold_font.render(text, 1, poker_constants.YELLOW)
        self.image = pygame.Surface([background_width, background_height])
        self.image.fill(fill_colour)
        self.rect = self.image.get_rect()
        self.rect.x = background_x
        self.rect.y = background_y
        W = self.text_surf.get_width()
        H = self.text_surf.get_height()
        if align == "right":
            self.image, self.image.blit(
                self.text_surf,
                [background_width - W - 20, background_height / 2 - H / 2],
            )
        if align == "left":
            self.image.blit(
                self.text_surf, [background_x - 50, background_height / 2 - H / 2]
            )
        return self.image, self.rect

    def draw_win_table(self, SCREEN):
        """Draws the win table"""
        pygame.draw.rect(SCREEN, poker_constants.YELLOW, (88, 9, 1102, 302))
        item_y = 10
        background_height = 30
        for lists in self.payout:
            for row in lists:
                item_x = 89
                for text in row:
                    if not text.startswith("£"):
                        background_width = 650
                        image_fist_column, rect_fist_column = Win_table.table_helper(
                            self,
                            text,
                            poker_constants.BLACK,
                            background_width - 1,
                            background_height,
                            item_x,
                            item_y,
                            "left",
                        )
                        SCREEN.blit(image_fist_column, rect_fist_column)
                    if text.startswith("£"):
                        background_colour = poker_constants.BLACK
                        background_width = 90
                        (
                            image_value_column,
                            rect_value_column,
                        ) = Win_table.table_helper(
                            self,
                            text,
                            background_colour,
                            background_width - 1,
                            background_height,
                            item_x,
                            item_y,
                            "right",
                        )
                        SCREEN.blit(image_value_column, rect_value_column)
                        if item_x == 739:
                            if self.bet == 1:
                                background_colour = poker_constants.LIGHT_RED
                                (
                                    image_value_column,
                                    rect_value_column,
                                ) = Win_table.table_helper(
                                    self,
                                    text,
                                    background_colour,
                                    background_width - 1,
                                    background_height,
                                    item_x,
                                    item_y,
                                    "right",
                                )
                                SCREEN.blit(image_value_column, rect_value_column)
                        if item_x == 829:
                            if self.bet == 2:
                                background_colour = poker_constants.LIGHT_RED
                                (
                                    image_value_column,
                                    rect_value_column,
                                ) = Win_table.table_helper(
                                    self,
                                    text,
                                    background_colour,
                                    background_width - 1,
                                    background_height,
                                    item_x,
                                    item_y,
                                    "right",
                                )
                                SCREEN.blit(image_value_column, rect_value_column)
                        if item_x == 919:
                            if self.bet == 3:
                                background_colour = poker_constants.LIGHT_RED
                                (
                                    image_value_column,
                                    rect_value_column,
                                ) = Win_table.table_helper(
                                    self,
                                    text,
                                    background_colour,
                                    background_width - 1,
                                    background_height,
                                    item_x,
                                    item_y,
                                    "right",
                                )
                                SCREEN.blit(image_value_column, rect_value_column)
                        if item_x == 1009:
                            if self.bet == 4:
                                background_colour = poker_constants.LIGHT_RED
                                (
                                    image_value_column,
                                    rect_value_column,
                                ) = Win_table.table_helper(
                                    self,
                                    text,
                                    background_colour,
                                    background_width - 1,
                                    background_height,
                                    item_x,
                                    item_y,
                                    "right",
                                )
                                SCREEN.blit(image_value_column, rect_value_column)
                        if item_x == 1099:
                            if self.bet == 5:
                                background_colour = poker_constants.LIGHT_RED
                                (
                                    image_value_column,
                                    rect_value_column,
                                ) = Win_table.table_helper(
                                    self,
                                    text,
                                    background_colour,
                                    background_width - 1,
                                    background_height,
                                    item_x,
                                    item_y,
                                    "right",
                                )
                                SCREEN.blit(image_value_column, rect_value_column)
                    item_x += background_width
                item_y += background_height
