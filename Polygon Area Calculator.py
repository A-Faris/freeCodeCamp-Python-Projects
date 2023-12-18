class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if (self.width or self.height) < 50:
            pic = list()
            for i in range(self.height):
                pic.append("*" * self.width + "\n")
            return "".join(pic)
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        return (self.width/shape.width * self.height/shape.height)

    def __str__(self):
        return ("Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")")

class Square(Rectangle):
    def __init__(self, side, width = int(), height = int()):
        super().__init__(width, height)
        self.width = side
        self.height = side
        
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        return ("Square(side=" + str(self.width) + ")")
