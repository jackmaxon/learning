class Contact:
    """
    Stores contact information for a user.
    """
    def __init__(self, first_name: str, last_name: str, phone: int = None, email: str = None, 
                 display_mode: str = "masked"):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        
        same_phone = self.phone == other.phone if self.phone is not None else False
        same_email = self.email == other.email if self.email is not None else False
        same_names = self.first_name == other.first_name and self.last_name == other.last_name

        return same_phone or same_email or same_names
    
    def __repr__(self):
        if self.display_mode == "masked":
            return self.mask_name
        else:
            return f"First Name: {self.first_name}, Last Name: {self.last_name}, Phone: {self.phone}, Email: {self.email}"
        
    def __str__(self):
        return f"{self.last_name[0]}{self.first_name[0]}"
    
    def __format__(self, format_spec: str):
        if format_spec == "reveal":
            return f"First Name: {self.first_name}, Last Name: {self.last_name}, Phone: {self.phone}, Email: {self.email}"
        
    def mask_name(self):
        return ''.join(['*' for _ in self.first_name]) + ' ' + ''.join(['*' for _ in self.last_name])

        
def test():
    user_1 = Contact("Jack", "Maxon", 1112223344, "jack@email.com", "masked")
    print(repr(user_1))

    user_2 = Contact("Jack", "Maxon")
    print(repr(user_2))

    user_3 = Contact("John", "Mayer", 1112223344, 'bob@email.com', "masked")
    print(user_1 == user_2)
    print(user_1 == user_3)
    print(user_2 == user_3)
    print(user_1)
    print(format(user_1, 'reveal'))

if __name__ == '__main__':
    test()