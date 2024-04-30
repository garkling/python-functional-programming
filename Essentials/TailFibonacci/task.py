from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:

    @tail_call_optimized
    def fibonacci(n: int, *, step: int = 1, curr: int = 1, prev: int = 0) -> int:
        if n < 2: return n
        if step >= n: return curr
        return fibonacci(n, step=step + 1, curr=curr + prev, prev=curr)

    return fibonacci
