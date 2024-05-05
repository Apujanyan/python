"""Custom python MRO"""


def merge(*mros):
    result = []
    while True:
        not_empty_mros = [mro for mro in mros if mro]
        if not not_empty_mros:
            return result
        for mro in not_empty_mros:
            candidate = mro[0]
            not_good_head = [h for h in not_empty_mros if candidate in h[1:]]
            if not_good_head:
                candidate = None
            else:
                break
        if not candidate:
            raise TypeError("Cannot create Method Resolution Order!")
        result.append(candidate)
        for m in not_empty_mros:
            if m[0] == candidate:
                del m[0]


def build_mro(cls):
    if cls == object:
        return [object]
    return [cls] + merge(*[build_mro(base) for base in cls.__bases__],
                               list(cls.__bases__))


def mro(cls):
    return tuple(build_mro(cls))



