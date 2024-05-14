"""
Liskov Substitution Principle

When extending a class, remember that you should be
able to pass objects of the subclass in place of objects of
the parent class without breaking the client code.
"""


# 1.
# Parameter types in a method of a subclass should match or
# be more abstract than parameter types in the method of the
# superclass.


class Animal:
    ...


class Cat(Animal):
    ...


class BengalCat(Cat):
    ...


class Feeder:
    def feed(self, obj: Cat) -> None:
        print(f'Feeder is feeding the {obj}!')


class ExtendedFeeder(Feeder):
    def feed(self, obj: Animal) -> None:
        print(f'Extended feeder is feeding the {obj}!')


# 2.
# The return type in a method of a subclass should match or be
# a subtype of the return type in the method of the superclass.


class CatShop:
    def buy_cat(self) -> Cat:
        return Cat()


class BengalCatShop(CatShop):
    def buy_cat(self) -> BengalCat:
        return BengalCat()


# 3.
# A method in a subclass shouldn’t throw types of exceptions
# which the base method isn’t expected to throw.


class ExtendedValueError(ValueError):
    ...


class Raiser:
    def raise_error(self) -> None:
        raise ValueError


class ExtendedRaiser(Raiser):
    def raise_error(self) -> None:
        raise ExtendedValueError


def catcher(error: Raiser):
    try:
        error.raise_error()
    except ValueError:
        print('I caught it!')


# 4.
# A subclass shouldn’t strengthen pre-conditions.


# Pre-condition has been strengthened!
class Base:
    def method(self, number: int) -> None:
        print('Works fine!')


class Derived(Base):
    def method(self, number: int) -> None:
        if number <= 0:
            raise ValueError
        print('Works fine with positive numbers!')


# 5.
# A subclass shouldn’t weaken post-conditions.


# Post-condition has been weakened!
class Super:
    def method(self, number: int) -> int:
        return abs(number)


class Sub(Super):
    def method(self, number: int) -> int:
        return number


# 6.
# Invariants of a superclass must be preserved.


# 7.
# A subclass shouldn’t change values of private
# fields of the superclass.
