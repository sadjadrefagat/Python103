from typing import List, Dict, Tuple, Any, Optional


def prod1(a, b):
    return a * b


def prod2(a: int, b: int, c: Optional[bool] = True) -> int:
    """
    returns product of a and b

    ---
    a is an integer


    ---
    b is aloso an integer
    """
    return a * b


print(prod2(10, 20))
