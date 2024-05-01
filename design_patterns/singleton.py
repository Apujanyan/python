"""Singleton design pattern example"""


class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


def main() -> None:
    s1 = Singleton()
    s2 = Singleton()
    print(f's1_id: {hex(id(s1))}')
    print(f's2_id: {hex(id(s2))}')


if __name__ == '__main__':
    main()
