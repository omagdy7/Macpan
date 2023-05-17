import pygame
import sys

from GUIbutton import Button, ToggleSwitch
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

        Debug_Mode = ToggleSwitch(image=pygame.image.load('../assets/Quit Rect.png'), pos=(300, 300),
                                  text_input="Debug Mode is OFF", font=get_font(20, 1), base_color="Black",
                                  hovering_color="cyan")

        Sound_Mode = ToggleSwitch(image=pygame.image.load('../assets/Quit Rect.png'), pos=(900, 300),
                                  text_input="Sound  ", font=get_font(20, 1), base_color="Black",
                                  hovering_color="cyan")

        # Debug_Mode_RECT = Debug_Mode.text.get_rect(center=(640, 150))

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        # Debug_Mode.changetext(OPTIONS_MOUSE_POS)
        # Debug_Mode.changeColor(OPTIONS_MOUSE_POS)
        Debug_Mode.update(SCREEN)
        #
        # #Sound_Mode.changeColor(OPTIONS_MOUSE_POS)
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
                        # Debug_Mode.update_image2(pygame.image.load('../assets/Quit Rect.png'))
                        # pygame.display.update()
                        Debug_Mode.changetext1()
                        Debug_Mode.update(SCREEN)
                        print(Debug_Mode.text_input)
                        print("Debug State  :")
                        print(lolsettings.debug)

                    else:
                        lolsettings.debug = True
                        Debug_Mode.changetext2()
                        Debug_Mode.update(SCREEN)
                        pygame.display.update()
                        print("Debug State  :")
                        print(lolsettings.debug)

                elif Sound_Mode.checkForInput(OPTIONS_MOUSE_POS):
                    if lolsettings.sound:
                        lolsettings.sound = False
                        print(lolsettings.sound)
                    else:
                        lolsettings.sound = True
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
                             text_input="PLAY", font=get_font(75, 2), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("../assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75, 2), base_color="#d7fcd4",
                                hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75, 2), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

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
