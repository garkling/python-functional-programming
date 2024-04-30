from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


def factorial_impl() -> Callable[[int], int]:

    @tail_call_optimized
    def factorial(n: int, *, step: int = 1, curr: int = 1) -> int:
        if n < 2: return 1
        if step >= n: return curr

        next_step = step + 1
        return factorial(n, step=next_step, curr=curr * next_step)

    return factorial
