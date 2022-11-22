import arcade
import random


class Comp151Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, 'Arcade Class Window Demo')
        self.player = None
        self.player_dx = 0
        self.player_dy = 0
        self.targets = arcade.SpriteList()
        self.score = 0
        self.sound1 = None

    def setup(self):
        self.sound1 = arcade.load_sound("elec_lightning.wav")
        self.player = arcade.Sprite("f1-ship1-6.png")
        self.player.center_x = 200
        self.player.center_y = 500
        for number in range(5):
            rock = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
            self.targets.append(rock)
            rock.center_x = random.randint(16, 1184)
            rock.center_y = random.randint(16, 984)

    def on_update(self, delta_time):
        self.player.center_x += self.player_dx
        if self.player.center_x > 1200:
            self.player.center_x = 0
            arcade.play_sound(self.sound1)
        if self.player.center_x < 0:
            self.player.center_x = 1200
            arcade.play_sound(self.sound1)
        if self.player.center_y > 1000:
            self.player.center_y = 0
            arcade.play_sound(self.sound1)
        if self.player.center_y < 0:
            self.player.center_y = 1000
            arcade.play_sound(self.sound1)
        self.player.center_y += self.player_dy

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = -3
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 3
        if symbol == arcade.key.UP:
            self.player_dy = 3
        elif symbol == arcade.key.DOWN:
            self.player_dy = -3

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player_dx = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player_dy = 0
