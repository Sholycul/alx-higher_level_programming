#!/usr/bin/python3

"""
Rectangele class

"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the ModuleClass.

        Parameters:
        - width (int): The width of the module.
        - height (int): The height of the module.
        - x (int, optional): The x-coordinate of the module's position. Default is 0.
        - y (int, optional): The y-coordinate of the module's position. Default is 0.
        - id (Any, optional): An identifier for the module. Default is None.

        Returns:
         None
         """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter

        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height  getter

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height  setter

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x  getter

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x  setter

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y  setter

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """
        Area of the rectangle
        """
        area = self.width * self.height
        return area


    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")


    def update(self, *args, **kwargs):
        """
        Updates the attributes of the ModuleClass instance.

        This method allows updating the module's attributes using positional arguments (*args) or keyword arguments (**kwargs).
        When using positional arguments, the order should be (id, width, height, x, y).

        Parameters:
        - args (tuple): Positional arguments to update the module's attributes in the order (id, width, height, x, y).
         - kwargs (dict): Keyword arguments to update specific attributes. Possible keys: 'id', 'width', 'height', 'x', 'y'.
    
        Returns:
        None
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v



    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

