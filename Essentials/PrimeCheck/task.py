def is_prime(n: int) -> bool:
    return n == 2 or not (
            n == 1 or
            n % 2 == 0 or
            any(n % div == 0 for div in range(3, int(n ** .5) + 1, 2))
    )
