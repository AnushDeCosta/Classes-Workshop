class Cat():
    """
    This is the class Cat that implements a cat with 3 attributes (name, nickname, cry and locations)
    """
    def __init__(self):
        self.name = "Pat"
        self.nickname = "FatPat"
        self.cry = "Meow"
        self.locations = []

    def speak(self):
        """
        Causes the cat to make its signature cry.
        :return: None – prints the cry sound to the console.
        """
        print(self.cry)


pat = Cat()
pat.speak()



