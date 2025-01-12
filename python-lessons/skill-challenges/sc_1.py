class Student:
    """
    Represents a student.
    """

    educational_platform = "udemy"
    greetings = [
                     "Hi I'm ", 
                     "Hey there, my name is ", 
                     "Hi. Oh, my name is "
                     ]

    def __init__(self, name, age = 22):
        self.name = name
        self.age = age

    def greet(self, greetings: list = greetings) -> str:
        """
        Randomly performs one of three pre-written greetings.
        """
        return random.choice(greetings) + str(self.name)