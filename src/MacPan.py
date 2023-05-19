import pygame
import sys

from GUIbutton import Button
from game import Game
import ctypes

from settings import Settings, settings

# icon on taskbar

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Pacman')

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mac-Pan")

BG = pygame.image.load("../assets/Background.png")

icon = pygame.image.load("../assets/icon.png")
pygame.display.set_icon(icon)

lolsettings = settings
lolsettings.debug = False


def get_font(size, number):  # Returns Press-Start-2P in the desired size
    if number == 1:
        return pygame.font.Font("../assets/PressStart2P-Regular.ttf", size)
    else:
        return pygame.font.Font("../assets/PAC-FONT.TTF", size)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#1e1f22")

        OPTIONS_TEXT = get_font(45, 1).render("OPTIONS SCREEN", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(630, 150))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 520),
                              text_input="BACK", font=get_font(75, 1), base_color="white", hovering_color="yellow")

        Debug_Mode = Button(image=pygame.image.load('../assets/Quit Rect.png'), pos=(300, 300),
                                  text_input="Debug Mode", font=get_font(20, 1), base_color="Black",
                                  hovering_color="yellow")

        Sound_Mode = Button(image=pygame.image.load('../assets/Quit Rect.png'), pos=(900, 300),
                                  text_input="Sound  ", font=get_font(20, 1), base_color="Black",
                                  hovering_color="yellow")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS, 'BACK', 'BACK')
        OPTIONS_BACK.update(SCREEN)
        Debug_Mode.update(SCREEN)
        Sound_Mode.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                    pygame.display.update()
                elif Debug_Mode.checkForInput(OPTIONS_MOUSE_POS):
                    if lolsettings.debug:
                        lolsettings.debug = False
                        print("Debug State  :")
                        print(lolsettings.debug)
                    else:
                        lolsettings.debug = True
                        print("Debug State  :")
                        print(lolsettings.debug)

                elif Sound_Mode.checkForInput(OPTIONS_MOUSE_POS):
                    if lolsettings.sound:
                        lolsettings.sound = False
                        print("Sound State  :")
                        print(lolsettings.sound)
                    else:
                        lolsettings.sound = True
                        print("Sound State  :")
                        print(lolsettings.sound)
        pygame.display.update()


def main_menu():
    # Initialize Pygame
    pygame.init()
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100, 2).render("Mac-Pan", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLaY", font=get_font(75, 2), base_color="#d7fcd4", hovering_color="#b68f40")
        OPTIONS_BUTTON = Button(image=pygame.image.load("../assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIoNS", font=get_font(75, 2), base_color="#d7fcd4",
                                hovering_color="#b68f40")
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(640, 550),
                             text_input="qUIT", font=get_font(75, 2), base_color="#d7fcd4", hovering_color="#b68f40")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON.changeColor(MENU_MOUSE_POS, "PLay", "PLAY")
        PLAY_BUTTON.update(SCREEN)

        OPTIONS_BUTTON.changeColor(MENU_MOUSE_POS, "oPTIoNs", "OPTIONS")
        OPTIONS_BUTTON.update(SCREEN)

        QUIT_BUTTON.changeColor(MENU_MOUSE_POS, "qUIT", "QUIT")
        QUIT_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game = Game(lolsettings)
                    game.run()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
