import unittest

class Tablet:
    """
    Represents a computing tablet.
    """
    MODELS = {
        "lite": [32, 2],
        "pro": [64, 3],
        "max": [128, 4]
    }

    def __init__(self, model: str):
        if model not in Tablet.MODELS:
            raise ValueError("Model must be chosen from 'lite', 'pro', or 'max'.")
        self.model = model
        self._added_storage = 0
        self._memory = Tablet.MODELS[self.model][1]
        self._base_storage = Tablet.MODELS[self.model][0]

    def add_storage(self, addition: int):
        if self.storage + addition > 1024:
            raise ValueError("Tablet only supports a maximum of 1024GB in storage.")
        self._added_storage += addition
    
    @property
    def storage(self):
        return self._base_storage + self._added_storage
    
    @storage.setter
    def storage(self, amount: int):
        if amount < self.base_storage:
            raise ValueError(f"Model {self.model} must have at least {self.base_storage}GB of base storage.")
        if amount > 1024:
            raise ValueError("Tablet only supports a maximum of 1024GB in storage.")
        self._added_storage = amount - self._base_storage 
    
    @property
    def base_storage(self):
        return self._base_storage

    @property
    def memory(self):
        return self._memory

    def __repr__(self):
        return f"Tablet(model='{self.model}', base_storage={self._base_storage}, added_storage={self._added_storage}, memory={self._memory})"
    
class TestTablet(unittest.TestCase):
    def test_initialization(self):
        lite_tablet = Tablet("lite")
        self.assertEqual(lite_tablet.model, "lite")
        self.assertEqual(lite_tablet.base_storage, 32)
        self.assertEqual(lite_tablet.memory, 2)
        self.assertEqual(lite_tablet.storage, 32)

    def test_invalid_model(self):
        with self.assertRaises(ValueError):
            Tablet("unknown")

    def test_add_storage(self):
        pro_tablet = Tablet("pro")
        pro_tablet.add_storage(32)
        self.assertEqual(pro_tablet.storage, 96)
        self.assertEqual(pro_tablet._added_storage, 32)

    def test_storage_setter_within_limit(self):
        max_tablet = Tablet("max")
        max_tablet.storage = 256
        self.assertEqual(max_tablet.storage, 256)
        self.assertEqual(max_tablet._added_storage, 128)

    def test_storage_setter_below_base_storage(self):
        max_tablet = Tablet("max")
        with self.assertRaises(ValueError):
            max_tablet.storage = 64

    def test_storage_setter_exceeding_limit(self):
        lite_tablet = Tablet("lite")
        with self.assertRaises(ValueError):
            lite_tablet.storage = 2048

    def test_repr(self):
        tablet = Tablet("pro")
        expected_repr = "Tablet(model='pro', base_storage=64, added_storage=0, memory=3)"
        self.assertEqual(repr(tablet), expected_repr)

if __name__ == "__main__":
    unittest.main()