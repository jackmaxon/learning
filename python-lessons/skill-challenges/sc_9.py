import unittest

class Point3D:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        order = ()
        for cls in self.__class__.__mro__:
            if hasattr(cls, "__slots__"):
                order = cls.__slots__ + order  # Concatenate tuples
        attrs = ', '.join(f"{attr}={getattr(self, attr)!r}" for attr in order if hasattr(self, attr))
        return f"{self.__class__.__name__}({attrs})"
    
class ColoredPoint(Point3D):
    __slots__ = ('color',)
    def __init__(self, x: int, y: int, z: int, color: str = 'black'):
        self.color = color
        super().__init__(x, y, z)

class ShapedPoint(Point3D):
    __slots__ = ('shape',)
    def __init__(self, x: int, y: int, z: int, shape: str = 'sphere'):
        self.shape = shape
        super().__init__(x, y, z)
class TestPoint3D(unittest.TestCase):
    def test_point3d_initialization(self):
        point = Point3D(1, 2, 3)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)
        self.assertEqual(point.z, 3)

    def test_point3d_repr(self):
        point = Point3D(4, 5, 6)
        self.assertEqual(repr(point), "Point3D(x=4, y=5, z=6)")

class TestColoredPoint(unittest.TestCase):
    def test_coloredpoint_initialization(self):
        point = ColoredPoint(1, 2, 3, "red")
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)
        self.assertEqual(point.z, 3)
        self.assertEqual(point.color, "red")

        # Test default color
        default_point = ColoredPoint(4, 5, 6)
        self.assertEqual(default_point.color, "black")

    def test_coloredpoint_repr(self):
        point = ColoredPoint(7, 8, 9, "blue")
        self.assertEqual(repr(point), "ColoredPoint(x=7, y=8, z=9, color='blue')")

class TestShapedPoint(unittest.TestCase):
    def test_shapedpoint_initialization(self):
        point = ShapedPoint(1, 2, 3, "cube")
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)
        self.assertEqual(point.z, 3)
        self.assertEqual(point.shape, "cube")

        # Test default shape
        default_point = ShapedPoint(4, 5, 6)
        self.assertEqual(default_point.shape, "sphere")

    def test_shapedpoint_repr(self):
        point = ShapedPoint(7, 8, 9, "pyramid")
        self.assertEqual(repr(point), "ShapedPoint(x=7, y=8, z=9, shape='pyramid')")

if __name__ == "__main__":
    unittest.main()
