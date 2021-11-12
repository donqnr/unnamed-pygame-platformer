from scripts import constants

class Cam():

    # Camera component, follows the player when they move around the level
    def __init__(self):
        super(Cam, self).__init__()
        self.x = 0
        self.y = 0
    
    # Get center of the screen in x axis
    def get_screen_center_x(self):
        return self.x - constants.SCREEN_WIDTH * .5
    # Get center of the screen in y axis
    def get_screen_center_y(self):
        return self.y - constants.SCREEN_HEIGHT * .5
    # Set camera's position in x axis
    def set_pos_x(self, set_x):
        self.x = -set_x
    # Set camera's position in y axis
    def set_pos_y(self, set_y):
        self.y = -set_y