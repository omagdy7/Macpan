from ghost import Ghost


class Blinky(Ghost):
    def __init__(self, sprite_sheet, x, y,settings):
        super().__init__(sprite_sheet, "red", x, y, settings)

