"""Custom classmethod descriptor. """


class Classmethod:
    def __init__(self, fn):
        self.__fn = fn

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self.__fn(owner, *args, **kwargs)
        return wrapper
