class PasswordGenerator:
    """
    Generates a password of described length and strength.

    :param strength: how strong the password should be, low, mid, or high.
    :param length: length of the password
    """
    INPUT_UNIVERSE = {
        "letters" : [chr(i) for i in range(ord('a'), ord('z') + 1)] + 
                    [chr(i) for i in range(ord('A'), ord('Z') + 1)],
        "numbers" : [str(i) for i in range(10)],
        "punctuation" : ["!", "?", ".", ",", ";", ":", "'", '"', "-", "_", "(", ")",
                        "[", "]", "{", "}", "@", "#", "$", "%", "&", "*", "+", 
                        "=", "/"]
    }

    DEFAULT_LENGTHS = {
        "low" : 8,
        "mid" : 12,
        "high": 16
    }


    def __init__(self, length: int = None, strength: str = "mid"):
        self.strength = strength or "mid"
        if self.strength not in self.DEFAULT_LENGTHS:
            raise ValueError("Invalid strength. Use 'low', 'mid', or 'high'.")

        self.length = length or self.DEFAULT_LENGTHS[strength]
        if not isinstance(self.length, int) or self.length <= 0:
            raise ValueError("Length must be a positive integer.")

        self.password = self._generate()

    def _generate(self) -> str:
        """
        Generates password of given (or default) length and strength using random 
        joining.
        """
        letters = self.INPUT_UNIVERSE["letters"]
        numbers = self.INPUT_UNIVERSE["numbers"]
        punctuation = self.INPUT_UNIVERSE["punctuation"]

        match self.strength:
            case "low":
                pool = letters
            case "mid":
                pool = letters + numbers
            case "high":
                pool = letters + numbers + punctuation

        return ''.join(random.choice(pool) for _ in range(length))

    @classmethod
    def show_input_universe(cls) -> dict:
        """
        Returns a dictionary containing the pools of characters from where sampling 
        is done.

        :return: The universe of characters from which random sampling is done to 
        generate passwords
        :rtype: dict (of list-s)
        """
        return cls.INPUT_UNIVERSE