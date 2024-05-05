"""Custom staticmethod descriptor"""


class Staticmethod:
    def __init__(self, fn):
        self.__fn = fn

    def __get__(self, instance, owner):
        return self.__fn
