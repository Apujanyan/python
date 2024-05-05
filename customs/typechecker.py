from functools import wraps
from typing import Callable


def typechecker(fn: Callable):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        annotations = fn.__annotations__
        for arg_name, arg_value in zip(fn.__code__.co_varnames, args):
            if arg_name in annotations:
                if not isinstance(arg_value, annotations[arg_name]):
                    raise TypeError(f"Argument {arg_name} must be of type "
                                    f"{annotations[arg_name]}!")
        for arg_name, arg_value in kwargs.items():
            if arg_name in annotations:
                if not isinstance(arg_value, annotations[arg_name]):
                    raise TypeError(f"Argument {arg_name} must be of type "
                                    f"{annotations[arg_name]}!")
        result = fn(*args, **kwargs)
        if 'return' in annotations.keys():
            if not isinstance(result, type(annotations['return'])):
                raise TypeError(f"Return type must be of type "
                                f"{annotations['return']}!")
    return wrapper
