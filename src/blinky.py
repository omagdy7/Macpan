from ghost import Ghost

class Blinky(Ghost):
    def __init__(self, sprite_sheet, x, y):
        super().__init__(sprite_sheet, "red", x, y)


