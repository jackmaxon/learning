# Jack Maxon
# Jan 6 2024
import random

class Tire:
    """
    Defines an autombile tire object.

    :param kind: the kind of tire, e.g., summer, spare, or winter
    :param distance_covered: the distance in km the the tire has covered
    """

    def __init__(self, kind: str, distance_covered: int):
        self.kind = kind
        self.distance_covered = distance_covered

class CapWords:
    # attributes of the class state
    doors = 2
    wheels = 4 # class atributes (avaliable under __dict__)
    tires = [Tire("Operational", 10) for i in range(4)]

    def __init__(self, color: str = "black"): # behavior of the class
        # __{name}__ are called dunders, reserved for methods
        # after instance creation, before the object is returned
        self.color = color

        # attributes are variables associated with objects

    def drive(self): # instance methods always take self as an argument
        return self
    
    @staticmethod
    def auto_drive(): 
        return "The car is auto driving for now..."
    
    @classmethod # Callable from the class object  
    def create_lease(cls):
        print(f"A lease for {cls} will be created")

    # create_lease = classmethod(create_lease)
    # auto_drive = staticmethod(auto_drive)

def main():
    print(type(CapWords))
    print(CapWords.__bases__) # base classes
    print(CapWords.__name__) # name of class

    m1 = CapWords() # instance of class
    m2 = CapWords() # another instance of the class
    print(m1 == m2) # returns False

    #### Video 6
    print(CapWords.__dict__)
    CapWords.model = 'G' # Added class attribute
    # Better practice to declare attributes in the class definition

    m3 = CapWords()
    m4 = CapWords()
    print(m4.model) # All new instances of the class will have the added attribute

    print(m3.drive())
    print(m3 == m3.drive())

    # When functions are defined within the body of a class, they become bound to 
    # instances of that class, and are then called methods

    print(getattr(m1, "color")) # equiv to m1.color
    setattr(m2, "color", "green") # sets attr

    objs = [m1, m2, m3]
    values = ["green", "yellow", "blue"]
    for obj in objs:
        for obj, val in zip(objs, values): 
            # zip combines the two lists into tuples by index
            setattr(obj, "color", val)

    try:
        m2.wingspan()
    except AttributeError as e:
        print(e)

    Jack = Student("Jack")
    print(Jack.greet())

    print(m1.__dict__)
    m1.__dict__["horse_power"] = 29 # __dict__ acts as expected
    print(m1.__dict__)

    # print(CapWords.__dict__)
    print(type(CapWords.__dict__))  # class dict is read only, unlike instances

    # we can declare individual instance properties
    m1.people = 5
    print(m1.people)
    
    # immutables: booleans, ints, floats, string, tuples 
    # i.e., we can't change their meaning in memory
    #
    # mutable: list

    print(m1.tires == m2.tires)

    m1.tired.append(Tire(kind="spare", distance_covered=100))

    print(m1.tires == m2.tires)

    # when we modify a class var, we modify it for all instances of the class

    # ... in python, every var is public
    
    m1.doors += 1

if __name__ == '__main__':
    main() 