from abc import ABC, abstractmethod


"""
Bridge

Bridge is a structural design pattern that lets you split a large
class or a set of closely related classes into two separate
hierarchies—abstraction and implementation—which can be
developed independently of each other.
"""


class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(
            self,
            x: float,
            y: float,
            radius: float
    ) -> None:
        ...


class DrawingAPI1(DrawingAPI):
    def draw_circle(
            self,
            x: float,
            y: float,
            radius: float
    ) -> None:
        print(f'API1 drawing circle at ({x}, {y}) with radius {radius}. ')


class DrawingAPI2(DrawingAPI):
    def draw_circle(
            self,
            x: float,
            y: float,
            radius: float
    ) -> None:
        print(f'API2 drawing circle at ({x}, {y}) with radius {radius}. ')


class Shape(ABC):
    def __init__(
            self,
            drawing_api: DrawingAPI
    ) -> None:
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        ...


class Circle(Shape):
    def __init__(
            self,
            drawing_api: DrawingAPI,
            x: float,
            y: float,
            radius: float
    ) -> None:
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)


def main() -> None:
    shape1 = Circle(DrawingAPI1(), 1, 2, 5)
    shape2 = Circle(DrawingAPI2(), 4, 5, 90)

    shape1.draw()
    shape2.draw()


if __name__ == '__main__':
    main()
