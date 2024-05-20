"""
Singleton

Singleton is a creational design pattern that lets you ensure
that a class has only one instance, while providing a global
access point to this instance.
"""


from threading import Lock, Thread


class Singleton(type):
    """Classic Singleton metaclass. """

    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonThreadSafe(type):
    """Thread-safe Singleton metaclass. """

    _instances: dict = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]