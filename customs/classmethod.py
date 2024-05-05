"""Custom classmethod descriptor"""


class Classmethod:
    def __init__(self, fn):
        self.__fn = fn

    def __get__(self, instance, owner):
        def class_method(*args, **kwargs):
            return self.__fn(owner, *args, **kwargs)
        return class_method
