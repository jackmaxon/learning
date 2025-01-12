import unittest

class DNABase:
    BASES = {
        "a": "adenine",
        "adenine": "adenine",
        "c": "cytosine",
        "cytosine": "cytosine",
        "g": "guanine",
        "guanine": "guanine",
        "t": "thymine",
        "thymine": "thymine"
    }

    def __init__(self, nucleotide: str):
        self.base = nucleotide

    def set_nucleotide(self, value: str):
        key = value.lower()
        if key not in self.BASES:
            raise ValueError(f"Value {value} is not allowed.")
        
        self._base = self.BASES[key]

    def get_nucleotide(self) -> str:
        return self._base

    def __repr__(self) -> str:
        return f"DNABase(base='{self._base}')"
    
    base = property(fget=get_nucleotide, fset=set_nucleotide)

class TestDNABase(unittest.TestCase):
    def setUp(self):
        self.dna1 = DNABase('Adenine')
        self.dna2 = DNABase('t')

    def test_initialization(self):
        self.assertEqual(self.dna1.base, 'adenine')
        self.assertEqual(self.dna2.base, 'thymine')

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            DNABase('InvalidBase')

    def test_case_insensitivity(self):
        dna = DNABase('A')
        self.assertEqual(dna.base, 'adenine')

    def test_repr(self):
        self.assertEqual(repr(self.dna1), "DNABase(base='adenine')")

    def test_setter_valid(self):
        self.dna1.base = 'C'
        self.assertEqual(self.dna1.base, 'cytosine')

    def test_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.dna1.base = 'InvalidBase'

if __name__ == "__main__":
    unittest.main()