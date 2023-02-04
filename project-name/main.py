"""Module docstring."""

print("Hello world")


def fnc(i: int):
    """
    Comment.

    Params:
    a: int
        some int
    """
    return f"yo {i}"


def func2(j: str):
    """
    Definitely not a numpy style docstring.

    Two lines
    Params:
    j

    """
    j = "a"
    print(j)
