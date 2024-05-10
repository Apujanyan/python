"""Factory method example"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self) -> None:
        ...


class Dog(Animal):
    def speak(self) -> None:
        print('Dog speaks!')


class Cat(Animal):
    def speak(self) -> None:
        print('Cat speaks!')


class Factory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        ...


class DogFactory(Factory):
    def create_animal(self) -> Dog:
        return Dog()


class CatFactory(Factory):
    def create_animal(self) -> Cat:
        return Cat()


def main() -> None:
    dog_factory = DogFactory()
    cat_factory = CatFactory()

    d1 = dog_factory.create_animal()
    c1 = cat_factory.create_animal()

    d1.speak()
    c1.speak()


if __name__ == '__main__':
    main()
