"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

"""

import arcade
import os
import math


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Serge's Arcade"
MOVEMENT_SPEED = 3


class Player(arcade.Sprite):
    """ Player class """

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the ship
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y        
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        
    def update(self):
            # Move the ball
            self.position_y += self.change_y
            self.position_x += self.change_x
    
            # See if the ball hit the edge of the screen. If so, change direction
            if self.position_x < self.radius:
                self.position_x = self.radius
    
            if self.position_x > SCREEN_WIDTH - self.radius:
                self.position_x = SCREEN_WIDTH - self.radius
    
            if self.position_y < self.radius:
                self.position_y = self.radius
    
            if self.position_y > SCREEN_HEIGHT - self.radius:
                self.position_y = SCREEN_HEIGHT - self.radius
                

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        
        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # Variables that will hold sprite lists
        self.player_list = None
        
        # Set up the player info
        self.player_sprite = None
        
        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)        

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        
    
    def update(self, delta_time):
            self.ball.update()
    
    def on_key_press(self, key, modifiers):
            """ Called whenever the user presses a key. """
            if key == arcade.key.LEFT:
                self.ball.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.ball.change_x = MOVEMENT_SPEED
            elif key == arcade.key.UP:
                self.ball.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.ball.change_y = -MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
            """ Called whenever a user releases a key. """
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.ball.change_x = 0
            elif key == arcade.key.UP or key == arcade.key.DOWN:
                self.ball.change_y = 0    

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.BLACK

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.AUBURN


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
