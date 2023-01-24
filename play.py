from constants.constants import SQUARE_SIZE, WHITE, BLACK
from checkers.game import Game
from algorithms.minimax import minimax
import pygame
import pygame_menu

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def play():
    pygame.init()
    pygame.display.set_caption('CHECKERS')
    window = pygame.display.set_mode((600, 600))

    flag = True
    clock = pygame.time.Clock()
    game = Game(window)

    while flag:
        clock.tick(60)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            pygame.init()
            screen = pygame.display.set_mode((600, 600), pygame.NOFRAME)

            theme_bg_image = pygame_menu.themes.THEME_ORANGE.copy()
            theme_bg_image.background_color = pygame_menu.BaseImage(
                image_path="assets/Background.png"
            )
            theme_bg_image.title_font_size = 25
            menu = pygame_menu.Menu(
                height=600,
                onclose=pygame_menu.events.EXIT,
                theme=theme_bg_image,
                title='GAME OVER!',
                width=600
            )
            MESSAGE = ""
            if game.winner() == WHITE:
                MESSAGE = "WHITE WON THIS GAME!"
            else:
                MESSAGE = "BLACK WON THIS GAME!"

            menu.add.label(MESSAGE, max_char=-1, font_size=30, font_color=(255, 255, 255), margin=(20, 150))
            menu.mainloop(screen)
            flag = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()