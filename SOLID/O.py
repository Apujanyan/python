from abc import ABC, abstractmethod


"""
Open/Closed Principle

Classes should be open for extension but closed for
modification.
"""


# Bad practice
class Order:
    def __init__(self, items, shipping: str) -> None:
        self.items = items
        self.shipping = shipping

    def set_shipping_type(self, value) -> None:
        if value not in ('air', 'ground'):
            raise ValueError('Unavailable shipping type!')
        self.shipping = value

    def get_shipping_cost(self) -> int:
        if self.shipping == 'air':
            return 100
        elif self.shipping == 'ground':
            return 50

    def get_shipping_date(self) -> str:
        if self.shipping == 'air':
            return '5 days.'
        elif self.shipping == 'ground':
            return '10 days.'


# Good practice
class Shipping(ABC):
    @abstractmethod
    def get_cost(self) -> int:
        ...

    @abstractmethod
    def get_date(self) -> str:
        ...


class GroundShipping(Shipping):
    def get_cost(self) -> int:
        return 100

    def get_date(self) -> str:
        return '5 days.'


class AirShipping(Shipping):
    def get_cost(self) -> int:
        return 50

    def get_date(self) -> str:
        return '10 days.'


class Order:
    def __init__(self, items, shipping: Shipping) -> None:
        self.items = items
        self.shipping = shipping

    def set_shipping_type(self, value) -> None:
        if not isinstance(value, Shipping):
            raise TypeError('Unavailable shipping type!')
        self.shipping = value

    def get_shipping_cost(self) -> int:
        return self.shipping.get_cost()

    def get_shipping_date(self) -> str:
        return self.shipping.get_date()



