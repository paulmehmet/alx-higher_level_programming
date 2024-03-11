class Square:

    def __init__(self, size=0, position=(0, 0)):

        self.size = size

        self.position = position

    

    @property

    def size(self):

        return self._size

    

    @size.setter

    def size(self, value):

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        if value < 0:

            raise ValueError("size must be >= 0")

        self._size = value

    

    @property

    def position(self):

        return self._position

    

    @position.setter

    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):

            raise TypeError("position must be a tuple of 2 positive integers")

        self._position = value

    

    def area(self):

        return self.size ** 2

    

    def my_print(self):

        if self.size == 0:

            print()

            return

        for _ in range(self.position[1]):

            print()

        for i in range(self.size):

            print(" " * self.position[0] + "#" * self.size)

    

    def __str__(self):

        res = []

        if self.size == 0:

            res.append("")

            return "\n".join(res)

        for _ in range(self.position[1]):

            res.append("")

        for i in range(self.size):

            res.append(" " * self.position[0] + "#" * self.size)

        return "\n".join(res)

    

    def __eq__(self, other):

        return isinstance(other, Square) and self.size == other.size

    

    def __ne__(self, other):

        return not self == other

    

    def __gt__(self, other):

        return isinstance(other, Square) and self.area() > other.area()

    

    def __ge__(self, other):

        return self > other or self == other

    

    def __lt__(self, other):

        return not self >= other

    

    def __le__(self, other):

        return not self > other


