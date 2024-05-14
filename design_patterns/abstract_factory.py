"""
Abstract Factory

Abstract Factory is a creational design pattern that lets you
produce families of related objects without specifying their
concrete classes.
"""


from abc import ABC, abstractmethod


class Shoes(ABC):
    @abstractmethod
    def get_price(self) -> None:
        ...


class Hat(ABC):
    @abstractmethod
    def get_price(self) -> None:
        ...


class SportShoes(Shoes):
    def get_price(self) -> None:
        print(f'The price of {self} is 50$.')


class ClassicShoes(Shoes):
    def get_price(self) -> None:
        print(f'The price of {self} is 100$.')


class SportHat(Hat):
    def get_price(self) -> None:
        print(f'The price of {self} is 10$.')


class ClassicHat(Hat):
    def get_price(self) -> None:
        print(f'The price of {self} is 20$.')


class ClothFactory(ABC):
    @abstractmethod
    def create_shoes(self) -> Shoes:
        ...

    @abstractmethod
    def create_hat(self) -> Hat:
        ...


class SportClothFactory(ClothFactory):
    def create_shoes(self) -> SportShoes:
        return SportShoes()

    def create_hat(self) -> SportHat:
        return SportHat()


class ClassicClothFactory(ClothFactory):
    def create_shoes(self) -> ClassicShoes:
        return ClassicShoes()

    def create_hat(self) -> ClassicHat:
        return ClassicHat()


def main() -> None:
    sport_factory = SportClothFactory()
    classic_factory = ClassicClothFactory()

    sport_shoes = sport_factory.create_shoes()
    sport_hat = sport_factory.create_hat()

    classic_shoes = classic_factory.create_shoes()
    classic_hat = classic_factory.create_hat()

    sport_shoes.get_price()
    sport_hat.get_price()

    classic_shoes.get_price()
    classic_hat.get_price()


if __name__ == '__main__':
    main()
