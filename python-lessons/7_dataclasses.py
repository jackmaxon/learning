## Jack Maxon
# Jan 16 2024
from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass, field
from functools import total_ordering
from typing import Any

class EV:
    def __init__(self, _range: int, make: str, price: int | float):
        self.range = _range # range is a reserved keyword
        self.make = make
        self.price = price

# @total_ordering # performance hit 
class EVehicle(NamedTuple):
    range: int 
    make: str
    price: int = 39000

@dataclass(order = True, frozen=True)
class ElectricVehicle:
    range: int =field(compare=True)
    make: str = field(default="Tesla", compare=False)
    price: int = field(default="56000", repr=False, compare=False)
    luxury: bool = False

    def __post__init__(self):
        luxury_brands = ["BMW", "Mercedez"]

        self.luxury = self.make in luxury_brands and self.price > 80000

# fuck da note class
def notes1():
    """Say we have some class EV and we want to store (range, make, and price) for a
    fleet of cars."""
    bolt = [417, "Chevy", 42000]
    model_s = [520, "tesla", 84000]
    # immutable? we could use a tuple. but we burden others by having index-specific 
    # fields. so we could use a dict
    EV(417, "Chevy", 42000)
    ev = namedtuple("ElectricVehicle", ["range", "make", "price"])
    ev1 = ev(417, "Chevy", 42000)
    print(ev1) # ElectricVehicle(range=417, make='Chevy', price=42000)
    print(ev1.range)

    # defaults set the rightmost attributes 
    ev = namedtuple("ElectricVehicle", ["range", "make", "price"], defaults=[100, "Tesla", 49000])
    # defaulted attrs cannot be followed by non defaulted attrs

    ev1._asdict()

    # can just specify using whitespace
    ev = namedtuple("ElectricVehicle", "range make price", defaults=[100, "Tesla", 49000])

    # named tuples attrs are immutable (private)
    ev = EVehicle(1, "t", 1)

def notes2():
    """
    Dataclasses.
    """
    ev = ElectricVehicle(1, "2", 1)
    # dataclasses good at storing state (data) with little code
    print(ev)

    # give us nice default repr, eq, 
    # @dataclass(order=True) gives > method, etc

    # dataclass fields are mutable
    # hashable if frozen
    # inheritance works as expected


if __name__ == '__main__':
    notes2()