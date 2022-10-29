"""New Math Functions"""

import math
from typing import Callable


def get_new_functions():
    return {
        "exp2": {
            "old": (math.exp, 4),
            "new": (math.exp2, 4),
        },
        "cbrt": {
            "old": (math.sqrt, 4),
            "new": (math.cbrt, 8),
        },
    }


def print_item(title: str, func: Callable[[int], float], value: int):
    print(f"\t{title}")
    print(f"\t\t# {func.__doc__}")
    print(f"\t\t{func.__name__}({value}) = {func(value):.2f}")


def main():
    for item_name, func in get_new_functions().items():
        print(f"New Function Name: {item_name!r}:")
        print_item("Like Previous:", *func["old"])
        print_item("Now we have", *func["new"])
        print()


if __name__ == "__main__":
    main()
