# Jack Maxon
# Jan 9 2024
import unittest

class Vector():
    def __init__(self, x: int, y: int, z: int):
        self.x_coord = x
        self.y_coord = y
        self.z_coord = z
        
    def __repr__(self):
        return f"Vector(x = {self.x_coord}, y = {self.y_coord}, z = {self.z_coord})"
    
    def __abs__(self):
        """
        Returns the magnitude of the vector (length).
        """
        return (self.x_coord ** 2 + self.y_coord ** 2 + self.z_coord ** 2) ** 0.5
    
    def __add__(self, other: "Vector"):
        if not isinstance(other, Vector):
            raise TypeError("Only instances of Vector may be added to Vector.")
        
        new_x = self.x_coord + other.x_coord
        new_y = self.y_coord + other.y_coord
        new_z = self.z_coord + other.z_coord

        return Vector(new_x, new_y, new_z)

    def __mul__(self, other: int | float):
        """
        Scalar multiplication.
        """
        if not isinstance(other, int | float):
            raise TypeError("Only instances of int and Vector may be multiplied.")
        
        new_x = self.x_coord * other
        new_y = self.y_coord * other
        new_z = self.z_coord * other
        
        return Vector(new_x, new_y, new_z)
    
    def __rmul__(self, other) -> "Vector":
        """
        Allows for right multiplication. Same implementation as __mul__.
        """
        return self * other

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(4, 5, 6)

    def test_repr(self):
        self.assertEqual(repr(self.v1), "Vector(x = 1, y = 2, z = 3)")

    def test_abs(self):
        self.assertAlmostEqual(abs(self.v1), (1**2 + 2**2 + 3**2)**0.5)

    def test_add(self):
        result = self.v1 + self.v2
        self.assertEqual(result.x_coord, 5)
        self.assertEqual(result.y_coord, 7)
        self.assertEqual(result.z_coord, 9)

    def test_mul(self):
        result = self.v1 * 2
        self.assertEqual(result.x_coord, 2)
        self.assertEqual(result.y_coord, 4)
        self.assertEqual(result.z_coord, 6)

    def test_rmul(self):
        result = 3 * self.v1
        self.assertEqual(result.x_coord, 3)
        self.assertEqual(result.y_coord, 6)
        self.assertEqual(result.z_coord, 9)

    def test_invalid_add(self):
        with self.assertRaises(TypeError):
            _ = self.v1 + 5

    def test_invalid_mul(self):
        with self.assertRaises(TypeError):
            _ = self.v1 * "string"

if __name__ == "__main__":
    unittest.main()