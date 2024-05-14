"""
Singleton

Singleton is a creational design pattern that lets you ensure
that a class has only one instance, while providing a global
access point to this instance.
"""


class Singleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DataBase(metaclass=Singleton):
    ...


d1 = DataBase()
d2 = DataBase()

print(d1 is d2)


