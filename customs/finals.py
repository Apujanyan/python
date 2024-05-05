"""Custom final metaclasses"""


class FinalInh(type):
    """Metaclass for preventing inheritance(runtime)"""

    def __new__(mcls, name, bases, cls_dict, **kwargs):
        for base in bases:
            if isinstance(base, FinalInh):
                raise TypeError(f'Cannot inherit from class {name}!')
        return super().__new__(mcls, name, bases, cls_dict)


class FinalOvr(type):
    """Metaclass for preventing attribute overriding(runtime)"""

    def __new__(mcls, name, bases, cls_dict, **kwargs):
        for base in bases:
            for attr in cls_dict.keys():
                if (
                    not attr in ('__module__', '__qualname__') and
                    attr in base.__dict__.keys()
                ):
                    raise TypeError(f'Cannot override attribute {attr}!')
        return super().__new__(mcls, name, bases, cls_dict, **kwargs)




