"""Abstract Factory design pattern example"""

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        ...


class CarShop(ABC):
    @staticmethod
    @abstractmethod
    def buy_car(car_name: str) -> Car:
        ...


class ElectricCar(Car):
    def __init__(self, name: str) -> None:
        self.name = name

    def start_engine(self) -> None:
        print(f'Starting engine of {self.name}!')


class GasolineCar(Car):
    def __init__(self, name:str) -> None:
        self.name = name

    def start_engine(self) -> None:
        print(f'Starting engine of {self.name}!')


class ElectricCarShop(CarShop):
    @staticmethod
    def buy_car(car_name: str) -> ElectricCar:
        print(f'Car {car_name} was successfully bought!')
        return ElectricCar(car_name)


class GasolineCarShop(CarShop):
    @staticmethod
    def buy_car(car_name: str) -> GasolineCar:
        print(f'Car {car_name} was successfully bought!')
        return GasolineCar(car_name)


def main() -> None:
    el_car = ElectricCarShop.buy_car('El_Car')
    gas_car = GasolineCarShop.buy_car('Gas_Car')
    el_car.start_engine()
    gas_car.start_engine()


if __name__ == '__main__':
    main()




