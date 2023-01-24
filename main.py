import re

import pygame
import pygame_menu
import sys

from constants.constants import LETTERS
from button import Button
from play import play
from algorithms.caesar import decrypt, encrypt


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


login_list_auth = []
password_list_auth = []


def auth_text_value_login(login):
    login_list_auth.append(login)


def auth_text_value_password(password):
    password_list_auth.append(password)


def auth_mistake():
    pygame.init()
    screen = pygame.display.set_mode((675, 375), pygame.NOFRAME)

    theme_bg_image = pygame_menu.themes.THEME_ORANGE.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path="assets/Background.png"
    )
    theme_bg_image.title_font_size = 25
    menu = pygame_menu.Menu(
        height=375,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='AUTHORIZATION',
        width=675
    )
    MESSAGE = "INCORRECT LOGIN OR PASSWORD"
    menu.add.label(MESSAGE, max_char=-1, font_size=30, font_color=(255, 255, 255), margin=(20, 150))
    menu.add.button('BACK', auth)
    menu.mainloop(screen)


def check():
    f = open('data_base.txt')
    s = f.read()
    split_string = re.split(r'[ \n]', s)
    if len(login_list_auth) != 0 and len(password_list_auth) != 0:
        if login_list_auth[-1] in split_string:
            if decrypt(split_string[split_string.index(login_list_auth[-1]) + 1]) == password_list_auth[-1]:
                play()
            else:
                auth_mistake()
        else:
            auth_mistake()
    else:
        auth_mistake()

    f.close()


def auth():
    pygame.init()
    screen = pygame.display.set_mode((675, 375), pygame.NOFRAME)

    theme_bg_image = pygame_menu.themes.THEME_ORANGE.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path="assets/Background.png"
    )
    theme_bg_image.title_font_size = 25
    menu = pygame_menu.Menu(
        height=375,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='AUTHORIZATION',
        width=675
    )

    menu.add.text_input('LOGIN: ', default='', onchange=auth_text_value_login,
                        valid_chars=valid_chars, font_size=40, font_color="#d7fcd4")

    menu.add.text_input('PASSWORD: ', default='', onchange=auth_text_value_password,
                        valid_chars=valid_chars, font_size=40, font_color="#d7fcd4", password=True)

    menu.add.button('OK', check, font_size=40, font_color="#d7fcd4")
    menu.add.button('MENU', main_menu, font_size=40, font_color="#d7fcd4")

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)

        pygame.display.update()


login_list_registration = []
password_list_registration = []


def registration_text_value_login(login):
    login_list_registration.append(login)


def registration_text_value_password(password):
    password_list_registration.append(password)


def registration_comlete():
    pygame.init()
    screen = pygame.display.set_mode((675, 375), pygame.NOFRAME)

    theme_bg_image = pygame_menu.themes.THEME_ORANGE.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path="assets/Background.png"
    )
    theme_bg_image.title_font_size = 25
    menu = pygame_menu.Menu(
        height=375,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='REGISTRATION',
        width=675
    )
    MESSAGE = "REGISTRATION COMPLETE!"
    menu.add.label(MESSAGE, max_char=-1, font_size=30, font_color=(255, 255, 255), margin=(20, 150))
    menu.add.button('BACK', main_menu)
    menu.mainloop(screen)


def write_in_registration_file():
    if len(login_list_registration) != 0 and len(password_list_registration) != 0:
        f = open('data_base.txt', 'a')
        f.write(login_list_registration[-1] + " " + encrypt(password_list_registration[-1]) + '\n')
        f.close()
        registration_comlete()


valid_chars = list(LETTERS)


def registration():
    pygame.init()
    screen = pygame.display.set_mode((675, 375), pygame.NOFRAME)

    theme_bg_image = pygame_menu.themes.THEME_ORANGE.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path="assets/Background.png"
    )
    theme_bg_image.title_font_size = 25
    menu = pygame_menu.Menu(
        height=375,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='REGISTRATION',
        width=675
    )

    menu.add.text_input('LOGIN: ', default='', onchange=registration_text_value_login,
                        valid_chars=valid_chars, font_size=40, font_color="#d7fcd4",
                        border_width=0)  # Function is bind here

    menu.add.text_input('PASSWORD: ', default='', onchange=registration_text_value_password, valid_chars=valid_chars,
                        password=True, font_size=40, font_color="#d7fcd4", border_width=0)  # Function is bind here

    menu.add.button('OK', write_in_registration_file, font_size=40, font_color="#d7fcd4", border_width=0)
    menu.add.button('MENU', main_menu, font_size=40, font_color="#d7fcd4", border_width=0)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)

        pygame.display.update()


def main_menu():
    pygame.init()
    SCREEN = pygame.display.set_mode((675, 375))
    pygame.display.set_caption("MENU")

    BG = pygame.image.load("assets/Background.png")
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(40).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(330, 70))

        AUTHORIZATION_BUTTON = Button(image=pygame.image.load("assets/Authorization.png"), pos=(330, 150),
                                      text_input="AUTHORIZATION", font=get_font(40), base_color="#d7fcd4",
                                      hovering_color="White")

        REGISTRATION_BUTTON = Button(image=pygame.image.load("assets/Registration.png"), pos=(330, 230),
                                     text_input="REGISTRATION", font=get_font(40), base_color="#d7fcd4",
                                     hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(330, 310),
                             text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [AUTHORIZATION_BUTTON, REGISTRATION_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AUTHORIZATION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    auth()
                if REGISTRATION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    registration()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
