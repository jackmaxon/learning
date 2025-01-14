## Jack Maxon
# Jan 12
from random import getrandbits, choice


# superclass, base class, parent class
class Virus:
    def __init__(self, name: str, reproduction_rate: float, resistance: float):
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.load = 1
        self.host = None

    def infect(self, host):
        self.host = host

    def reproduce(self):
        if self.host is not None:
            self.load *= (1 + self.reproduction_rate)

            should_mutate = getrandbits(1)
            print(f"Should mutate: {should_mutate}.")

            if should_mutate:
                try:
                    self.mutate()
                except AttributeError:
                    pass

            return True, f"Virus reproduced in {self.host}. Viral load: {self.load}."
        
        raise AttributeError("Virus needs to infect a host before being able to reproduce.")

# derived class, child class, subclass, subtype
class RNAVirus(Virus):
    genome = "ribonucleic"
    
    def reproduce(self):
        success, status = Virus.reproduce(self)
        if success:
            print(f"{self.name} just replicated in the cytoplasm of {self.host} cells.")

class DNAVirus(Virus):
    genome = "deoxyribonucleic"
    
    def reproduce(self):
        success, status = Virus.reproduce(self)
        if success:
            print(f"{self.name} just replicated in the cytoplasm of {self.host} cells.")

class CoronaVirus(RNAVirus):
    def infect(self, host):
        print("A coronavirus specific method with different signature than the parent's")
        self.host = host
        # raise NotImplementedError()
    
class SARSCov2(CoronaVirus):
    known_variants = ["alpha", "beta", "gamma", "epsilon"]
    def __init__(self, variant):
        super().__init__("SARSCOV2", 2.49, 1.3)
        self.variant = variant

    def mutate(self):
        print(f"The {self.name} virus just mutated in its spike protein.")

    @property
    def variant(self):
        return self._variant

    @variant.setter
    def variant(self, value):
        if value.lower() not in self.known_variants:
            raise ValueError("Expected a known variant of concern")
        
        self._variant = value.lower()

class DoubleMutant(SARSCov2):
    @SARSCov2.variant.setter
    def variant(self, value):
        self._variant = value.lower()

class FunnyDict(dict):
    not_found = ['404', 'Wait, where?', 'Try again, or dont?']
    def __getitem__(self, key):
        if key not in self:
            return choice(self.not_found)
        return super().__getitem__(key)

class AvgList(list):
    def __init__(self, *args):
        if args and type(args[0]) != list:
            super().__init__(args)
        else:
            super().__init__(args[0])
    @property
    def average(self):
        return sum(self) / len(self)

class VideoNotes:
    V = Virus("chandipura", 1.2, 1.1)
    R = RNAVirus("HIV", 1.1, 0.2)


    @staticmethod
    def idea1():
        """
        class inheritance
        """
        V = VideoNotes.V
        V.infect("human")
        V.reproduce()

        R = VideoNotes.R
        R.infect("monkey")
        R.reproduce()

        # All user-defined classes are subclasses of object
        # object is callable because its type implements __call__
        # object exists to give basic functionality to all classes
    
    @staticmethod
    def idea2():
        """
        """
        # resolution order:
        # instance -> class -> superclass(class) -> ... -> object, else AttributeError

        V = VideoNotes.V
        print(Virus.__bases__) # object
        print(RNAVirus.__mro__) # method resolution order

        # lowest level method in this chain "wins" and is called
        cv = CoronaVirus("MERS", .1, .2)
        # cv.infect()

        cv2 = SARSCov2("original", 2.9, 1.2)
        cv2.infect("John")
        for _ in range(4):
            print(cv2.reproduce())

    @staticmethod
    def idea3():
        """
        super() returns an instance of the parent class
        """
        pass
        # usually init it passed to super()
        cv = SARSCov2("beta")
        # missing parent attributes
        print(cv.__dict__)

        # misuse: parent - child class relationship
        # child defines an init only for the purpose of calling parent init

        print(cv.__dict__)
        dv = DoubleMutant("NEW")
        print(dv.variant) 

    @staticmethod
    def idea4():
        """
        """
        population = FunnyDict({
            "CAN": 38,
            "USA": 329,
            "IND": 1380
        })
        population['CANADA'] # Key value error thrown by __getitem__

        l = AvgList([1,10,2.23,21])
        l2 = AvgList(1,2,3,4)

        population.get("CAN")
        # 
        # self.get not implemented in our implementation of funny dict
        # we can get around this using the collections module

if __name__ == '__main__': 
    VideoNotes.idea4()