import arcade
from ShipMain import ShipWindow


def main():
    window = ShipWindow()
    arcade.set_background_color(arcade.color.SEA_BLUE)
    window.setup()
    arcade.run()


main()
