from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass
class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width
    def draw(self) -> None:
        for i in range(1, self.width + 1):
            print('*' * i)
class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    def draw(self) -> None:
        for _ in range(self.height):
            print('*' * self.width)

shapes = [Triangle(10), Rectangle(5, 4)]

for shape in shapes:
    shape.draw()
    print()
