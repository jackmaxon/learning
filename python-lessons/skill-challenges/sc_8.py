from typing import Hashable
from collections import UserDict

class BidirectionalDict(dict):
    """
    Dict which allows reverse lookups.
    """
    def __init__(self, dictionary: dict = None):
        super().__init__()
        if dictionary is not None:
            for key, value in dictionary.items():
                self[value] = key # reverse mapping
        else:
            raise ValueError("Item is not a dictionary")

    def __setitem__(self, key: Hashable, value: Hashable) -> None:
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        super().__setitem__(key, value)
        super().__setitem__(value, key)
        return value

    def __delitem__(self, key: Hashable) -> None:
        value = self[key]
        super().__delitem__(key)
        super().__delitem__(value)

    def __len__(self) -> int:
        return super().__len__() // 2
    