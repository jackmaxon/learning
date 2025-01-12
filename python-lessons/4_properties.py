## Jack Maxon
# Jan 10 2024

class Customer:
    """
    Represents a customer.
    """
    loyalty_levels = {"Bronze", "Gold", "Platinum"}

    def __init__(self, loyalty: str, membership: int = 0):
        # self.set_loyalty = loyalty 
        self.loyalty = loyalty
        self.membership = membership
        self._reviews = []
        self._avg_review = None

    def set_membership(self, value: int):
        if value < 0 or value > 34:
            raise ValueError(f"Invalid membership years")

        self._membership = value

    def get_membership(self):
        return self._membership

    loyalty = property()

    def add_review(self, review):
        if not(type(review) == int or 0<= review <= 10):
            raise ValueError

        self._reviews.append(review)
        self._avg_review = None if review != self._avg_review else review

    @property 
    def average_review(self):
        if self._avg_review is None:
            return sum(self._reviews) / len(self._reviews)
        return self._avg_review

    @property
    def loyalty(self):
        """
        A property that returns the loyalty level of the customer.
        Setting and deleting is also supported.
        """
        return self._loyalty
    
    @loyalty.setter
    def loyalty(self, level: str):
        if level not in self.__class__.loyalty_levels:
            raise ValueError(f"Invalid loyalty {level} specified.")
        
        self._loyalty = level

    @loyalty.deleter
    def loyalty(self):
        del self._loyalty

    # loyalty = property(fget=get_loyalty, fset=set_loyalty)
    # membership = property(fget=get_membership, fset=set_membership)

def get_discount(customer: Customer):
    discounts = {
        "Bronze": .1,
        "Gold": .2,
        "Platinum": .35
    }

    discount = discounts.get(customer.get_loyalty, None)

    if not discount:
        raise ValueError("Could not determine the customer's discount!")
    
    return discount

class VideoNotes:

    c_1 = Customer("Bronze")
    c_2 = Customer("Gold")
    c_3 = Customer("Platinum")

    @staticmethod
    def idea1():
        """
        Can access class traits from outside of class (no private vars)
        """
        for customer in [VideoNotes.c_1, VideoNotes.c_2, VideoNotes.c_3]:
            print(f"Your discount is {get_discount(customer):.0%}")

    @staticmethod
    def idea2():
        """
        """
        c = Customer("Andy") 
        c2 = Customer("Bronze")
        # c2._loyalty = "Andy" # skip validation logic
        # _attr implies intent
        # __attr mangles attr with class name

    @staticmethod
    def idea3():
        """
        Properties
        """
        # loyalty = property(fget=get_loyalty, fset=set_loyalty)
        # so all sets must got through set_loyalty, all gets must go through get_loyalty
        C = Customer("Gold", 23)
        C.membership += 1

        C.__dict__["_loyalty"] = 'Platinum'
        # since loyalty is a property, when called it is redirected to its getter/setter

        # all the properties we define live in the class' mapping proxy, 
        # not the instance dict
        # instance attr that have the same name as a prop do not shadow the workings 
        # of the prop

    @staticmethod
    def idea4():
        """
        Decorators
        """
        C = Customer("Gold")
        # can use loyalty = property()
        # loyalty = loyalty.getter(loyalty_getter)
        # or use 
        # @property_name (setter)
        # @property_name.getter

        def ten_times(x):
            return x * 10
        
        ten_x = ten_times
        print(ten_x(10))

        def pass_three_to(func): # composition of functions
            what = 3
            return func(what)

        print(pass_three_to(ten_x))

        # Closures
        def greet(who):
            how = "Good morning"

            def create_greeting():
                print(f"{how}, {who}!")

            return create_greeting

        a = greet("andy")
        a()

        from random import randint

        

        def even_or_odd(func):
            def inner():
                num = func()
                print(f"The selected number is {'even' if num % 2 ==0 else 'odd'}")
            return inner

        @even_or_odd
        def bingo():
            return randint(1,47)
        # bingo = even_or_odd(bingo)
        bingo()

    @staticmethod
    def idea5():
        """
        R/W, managed attributes 
        """
        # if we define no setter it is a read only property
        # conversely, a write only property 
        c = Customer("Gold")
        c.add_review(3)
        c.add_review(10)
        print(c.average_review)

        del c.loyalty # deletes it from the instance, not the class
        print(c.__dict__)
        # property(fget, fset, fdel, doc)


if __name__ == '__main__':
    VideoNotes.idea5()