from typing import Callable


def fibonacci_impl() -> Callable[[int], int]:
    def fibonacci(n: int) -> int:
        return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci
