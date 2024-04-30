from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    i1 = Integer(1)
    i2 = Integer(2)

    for i in (i1, i2):
        if not (
            isinstance(increment_fn(i), Integer) and
            increment_fn(i).value == i.value + 1 and
            increment_fn(i).value == increment_fn(i).value
        ): return False

    return increment_fn(i1).value != increment_fn(i2).value
