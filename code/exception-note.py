# add_note to Exception

import random
import math


def solve(xf, yf, zf):
    "solve xf*x^2 + yf*y + zf*z = 0 Eq."
    delta = math.sqrt(yf**2 - 4 * xf * zf)
    return (-yf - delta, -yf + delta)


def fuzzy_test(func, trials: int):
    for i in range(trials):
        x = random.randint(-15, 15)
        y = random.randint(-15, 15)
        z = random.randint(-15, 15)
        try:
            func(x, y, z)
        except Exception as ex:
            ex.add_note(
                f"There was an error in the function: {func.__name__}({x}, {y}, {z})"
            )
            raise


def add_note_to_exception():
    fuzzy_test(solve, 100)


if __name__ == "__main__":
    add_note_to_exception()
