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
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if max(self.width, self.height) > 50:
            return "Too big for picture."

        return (("*" * self.width + "\n") * self.height)

    def get_amount_inside(self, shape):
        fit_width = self.width // shape.width
        fit_height = self.height // shape.height
        return fit_width * fit_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"

def ejemplo():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

def tests():
    # 4. The string representation of `Rectangle(3, 6)` should be `'Rectangle(width=3, height=6)'`.
    assert str(Rectangle(3, 6)) == 'Rectangle(width=3, height=6)'
    # 5. The string representation of `Square(5)` should be `'Square(side=5)'`.
    assert str(Square(5)) == 'Square(side=5)'
    # 6. `Rectangle(3, 6).get_area()` should return `18`.
    assert Rectangle(3, 6).get_area() == 18
    # 7. `Square(5).get_area()` should return `25`.
    assert Square(5).get_area() == 25
    # 8. `Rectangle(3, 6).get_perimeter()` should return `18`.
    assert Rectangle(3, 6).get_perimeter() == 18
    # 9. `Square(5).get_perimeter()` should return `20`.
    assert Square(5).get_perimeter() == 20
    # 10. `Rectangle(3, 6).get_diagonal()` should return `6.708203932499369`.
    assert Rectangle(3, 6).get_diagonal() == 6.708203932499369
    # 11. `Square(5).get_diagonal()` should return `7.0710678118654755`.
    assert Square(5).get_diagonal() == 7.0710678118654755
    # 18. `Rectangle(15,10).get_amount_inside(Square(5))` should return `6`.
    assert Rectangle(15,10).get_amount_inside(Square(5)) == 6
    # 19. `Rectangle(4,8).get_amount_inside(Rectangle(3, 6))` should return `1`.
    assert Rectangle(4,8).get_amount_inside(Rectangle(3, 6)) == 1
    # 20. `Rectangle(2,3).get_amount_inside(Rectangle(3, 6))` should return `0`.
    assert Rectangle(2,3).get_amount_inside(Rectangle(3, 6)) == 0
    #
    return True

if __name__ == '__main__':
    ejemplo()
    print(f"\nTodos los tests pasaron\n") if tests() else print(f"\nError en los tests\n")
