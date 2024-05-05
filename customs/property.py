"""Custom property descriptor"""


class Property:
    def __init__(
            self,
            fget=None,
            fset=None,
            fdel=None,
            doc=None
    ):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc

    def __get__(self, instance, owner) -> None:
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('Unreadable attribute!')

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('Cannot set the attribute!')
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('Cannot delete the attribute!')
        self.fdel(instance)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.doc)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.doc)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.doc)



