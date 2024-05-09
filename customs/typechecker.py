"""Typechecker decorator for class __init__ type checking"""

def typechecker(cls):
    def wrapper(*args, **kwargs):
        init = cls.__init__
        types = init.__annotations__
        var_names = init.__code__.co_varnames[1::]

        # For positional arguments
        for arg_value, arg_name in zip(args, var_names):
            if arg_name in types:
                if not isinstance(arg_value, types[arg_name]):
                    raise TypeError(f"Expected {types[arg_name]}, "
                                    f"got {type(arg_value)}!")

        # For keyword arguments
        for arg_name, arg_value in kwargs.items():
            if arg_name in types:
                if not isinstance(arg_value, types[arg_name]):
                    raise TypeError(f"Expected {types[arg_name]}, "
                                    f"got {type(arg_value)}!")
        return cls(*args, **kwargs)
    return wrapper





