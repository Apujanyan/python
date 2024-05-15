from abc import ABC, abstractmethod


"""
Bridge

Bridge is a structural design pattern that lets you split a large
class or a set of closely related classes into two separate
hierarchies—abstraction and implementation—which can be
developed independently of each other.
"""


class Window(ABC):
    @abstractmethod
    def open(self) -> None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def size_increase(self) -> None:
        ...

    @abstractmethod
    def size_decrease(self) -> None:
        ...

    @abstractmethod
    def is_opened(self) -> bool:
        ...


class WindowManager:
    def __init__(self, window: Window) -> None:
        self.window = window

    def open(self) -> None:
        self.window.open()

    def close(self) -> None:
        self.window.close()

    def toggle(self) -> None:
        if self.window.is_opened():
            self.window.close()
        else:
            self.window.open()

    def increase(self) -> None:
        self.window.size_increase()

    def decrease(self) -> None:
        self.window.size_decrease()


class UnixWindow(Window):
    __counter = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.size = 100

    def open(self) -> None:
        print(f'{self.name} is opened!')
        self.__counter += 1

    def close(self) -> None:
        print(f'{self.name} is closed!')
        self.__counter += 1

    def size_increase(self) -> None:
        self.size += 10
        print(f'{self.name}\'s size is {self.size}!')

    def size_decrease(self) -> None:
        self.size -= 10
        print(f'{self.name}\'s size is {self.size}!')

    def is_opened(self) -> bool:
        if self.__counter % 2 == 1:
            return True
        return False


def main() -> None:
    vim = UnixWindow('VIM')
    manager = WindowManager(vim)

    manager.open()
    manager.toggle()
    manager.increase()
    manager.toggle()


if __name__ == '__main__':
    main()

