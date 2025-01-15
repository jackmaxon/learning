class Employee:
    __slots__ = ('name', 'surname', 'age', 'status', 'salary')

    def __init__(self, name: str, surname: str, age: int, status: str, salary: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.status = status
        self.salary = salary

    # @property
    # def high_salary(self):
    #     return self.salary > 300000 

class Developer(Employee):
    pass

class Notes:
    """
    Video notes.
    """
    o1 = Employee("andrew", "dorthy", 42, "FT", 400000)

    def one():
        """
        """
        print(Notes.o1)
        # memory overhead in storing namespace (instance, class)
        # adding slots dunder removes __dict__ support
        # moves data from infinite dict to finite 'slots'

        # dict eats up lots of memory, as dict is a hash map O(n)
        # compared to O(1) for arrays (slot, written in c)
        print(Employee.__dict__)

        # both properties and slotted attributes are descriptors (get, set, delete)

        d = Developer("A", "A", 23, "A", 1)
        print(d.__dict__) # still has dict

        # if a parent class is not slotted, the child class will have an class namespace
        # even if it is slotted

if __name__ == '__main__':
    Notes.one()