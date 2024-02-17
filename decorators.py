class Square:
    # Setup constructor
    def __init__(self, w, h):
        self.__height = h
        self.__width = w

    # Make use of @property decorators
    @property
    def height(self):
        return self.__height
    
    @property
    def width(self):
        return self.__width

    # Create setters to modify values
    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("Height value must be larger than 0")
        
    @width.setter
    def width(self, new_value):
        if new_value >= 0:
            self.__width = new_value
        else:
            raise Exception("Width value must be larger than 0")

# Instantiate a new object and print to console with @property
square = Square(0, 0)
print("The new object has a height of " + str(square.height) + " and a width of " + str(square.width))

# Set new values with setters for existing square
square.height = 4
square.width = 4
print("The object values changed with setters has a height of " + str(square.height) + " and a width of " + str(square.width))