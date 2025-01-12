## Jack Maxon
# Jan 12
from random import getrandbits


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
    def __init__(self, variant):
        super().__init__("SARSCOV2", 2.49, 1.3)
        self.variant = variant

    def mutate(self):
        print(f"The {self.name} virus just mutated in its spike protein.")

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
        cv = SARSCov2("Omicron")
        # missing parent attributes
        print(cv.__dict__)

        # misuse: parent - child class relationship
        # child defines an init only for the purpose of calling parent init

if __name__ == '__main__':
    VideoNotes.idea3()