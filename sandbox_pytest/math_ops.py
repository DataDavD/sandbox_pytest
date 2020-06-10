from functools import reduce
from typing import Sequence, Union


def add(*args: Union[Sequence[int], int]) -> int:
    if isinstance(args, int):
        result = reduce((lambda x, y: x + y), args)
        return result
    else:
        result = reduce((lambda x, y: x + y), *args)
        return result


def sub(*args: Union[Sequence[int], int]) -> int:
    if isinstance(args, int):
        result = reduce((lambda x, y: x - y), args)
        return result
    else:
        result = reduce((lambda x, y: x - y), *args)
        return result


def multiply(*args: Union[Sequence[int], int]) -> int:
    if isinstance(args, int):
        result = reduce((lambda x, y: x * y), args)
        return result
    else:
        result = reduce((lambda x, y: x * y), *args)
        return result


def div(*args: Union[Sequence[int], int]) -> int:
    if isinstance(args, int):
        result = reduce((lambda x, y: x / y), args)
        return result
    else:
        result = reduce((lambda x, y: x / y), *args)
        return result
