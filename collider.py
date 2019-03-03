class Collider:

    def __init__(self, tag, width, height):

        self.enabled = True
        self.tag = tag
        self.width = width
        self.height = height
        self.pos_x = 0
        self.pos_y = 0

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def check_collision(self, col):

        if self.enabled is False:
            return

        if col.pos_x + col.width >= self.pos_x and col.pos_x <= self.pos_x + self.width:
            if col.pos_y + col.height >= self.pos_y and col.pos_y <= self.pos_y + self.height:
                return True

        return False