"""Typechecker decorator for class __init__ type checking. """


def typecheck(cls):
    """Type checker decorator as function. """

    def wrapper(*args, **kwargs):
        init = cls.__init__
        types = init.__annotations__
        var_names = init.__code__.co_varnames[1::]

        # For positional arguments
        for arg_value, arg_name in zip(args, var_names):
            if arg_name in types:
                if not isinstance(arg_value, types[arg_name]):
                    raise TypeError(f"Argument {arg_name} expected "
                                    f"{types[arg_name].__name__}")

        # For keyword arguments
        for arg_name, arg_value in kwargs.items():
            if arg_name in types:
                if not isinstance(arg_value, types[arg_name]):
                    raise TypeError(f"Argument {arg_name} expected "
                                    f"{types[arg_name].__name__}")

        return cls(*args, **kwargs)
    return wrapper


class Typecheck:
    """Type checker decorator as class. """

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        init = self.cls.__init__
        types = init.__annotations__
        varnames = init.__code__.co_varnames[1::]

        # For positional arguments
        for arg_name, arg_value in zip(varnames, args):
            if arg_name in types:
                if not isinstance(arg_value, types[arg_name]):
                    raise TypeError(f"Argument {arg_name} expected "
                                    f"{types[arg_name].__name__}")

        # For keyword arguments
        for arg_name, arg_value in kwargs.items():
            if arg_name in types:
                if not isinstance(arg_value, types[arg_name]):
                    raise TypeError(f"Argument {arg_name} expected "
                                    f"{types[arg_name].__name__}")

        return self.cls(*args, **kwargs)
