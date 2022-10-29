# New Math Functions

import math

new_functions = {
    "exp2": {
        "old": (math.exp, 4),
        "new": (math.exp2, 4),
    },
    "cbrt": {
        "old": (math.sqrt, 4),
        "new": (math.cbrt, 8),
    },
}


def print_item(title: str, func, value):
    print(f"\t{title}")
    print(f"\t\t# {func.__doc__}")
    print(f"\t\t{func.__name__}({value}) = {func(value):.2f}")


def main():
    for item_name, func in new_functions.items():
        of, ov = func["old"]
        nf, nv = func["new"]
        print(f"New Function Name: {item_name!r}:")
        print_item("Like Previous:", of, ov)
        print_item("Now we have", nf, nv)
        print()


if __name__ == "__main__":
    main()
